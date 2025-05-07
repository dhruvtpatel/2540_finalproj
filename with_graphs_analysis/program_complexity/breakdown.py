import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
from collections import defaultdict
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

def normalize_program_name(name):
    """Normalize program names to handle variations in different result files."""
    # Remove any suffixes like "_transformed" or ".py" or "_module"
    name = re.sub(r'(_transformed|\.py|_module\.py|_module)$', '', name)
    return name

# Extract data from program_difficulty_scores.json and verification/all_results.json
def extract_data_from_json():
    try:
        # Read the program difficulty scores JSON file
        difficulty_path = os.path.join(PROJECT_ROOT, "difficulty/program_difficulty_scores.json")
        if not os.path.exists(difficulty_path):
            print(f"Error: Difficulty scores file not found at {difficulty_path}")
            return None, None, None
            
        with open(difficulty_path, "r") as f:
            program_data = json.load(f)
        
        # Read the verification results JSON file
        verification_path = os.path.join(PROJECT_ROOT, "verification/all_results.json")
        if not os.path.exists(verification_path):
            print(f"Error: Verification results file not found at {verification_path}")
            return None, None, None
            
        with open(verification_path, "r") as f:
            verification_data = json.load(f)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None, None, None
    
    # Create a dictionary of verification results for easier lookup
    verification_results = {}
    
    # Create a dictionary to track false positives from FEQ data
    false_positives = {}
    
    # Load FEQ data to identify false positives
    try:
        feq_path = os.path.join(PROJECT_ROOT, "verification", "failure_explanation_quality", "feq_evaluation_results.json")
        if os.path.exists(feq_path):
            with open(feq_path, "r") as f:
                feq_data = json.load(f)
                
            # Process FEQ data to identify false positives
            for entry in feq_data:
                function_name = normalize_program_name(entry.get("function", ""))
                method = entry.get("method", "").lower()
                is_false_positive = entry.get("false_positive", False)
                
                if is_false_positive:
                    if function_name not in false_positives:
                        false_positives[function_name] = set()
                    false_positives[function_name].add(method)
    except Exception as e:
        print(f"Warning: Could not load FEQ data to identify false positives: {str(e)}")
        false_positives = {}
    
    # Process verification results
    for result in verification_data:
        program_name = result["program"]
        normalized_program = normalize_program_name(program_name)
        
        # Get FEQ values - use numeric values when available, "NA" otherwise
        feq_crosshair = result.get("feq", {}).get("crosshair", "NA")
        if feq_crosshair != "NA" and isinstance(feq_crosshair, (int, float)):
            feq_value = float(feq_crosshair)  # Use CrossHair FEQ as the primary value
        else:
            # Try Nagini FEQ if CrossHair isn't available
            feq_nagini = result.get("feq", {}).get("nagini", "NA")
            feq_value = float(feq_nagini) if feq_nagini != "NA" and isinstance(feq_nagini, (int, float)) else 0.5
        
        # Handle different types of status values, including 'inconclusive' for false positives
        fuzz_status = result.get("fuzz", "").lower()
        crosshair_status = result.get("crosshair", "").lower()
        nagini_status = result.get("nagini", "").lower()
        
        # Check if any results should be marked as inconclusive due to being false positives
        is_fuzz_false_positive = normalized_program in false_positives and "fuzz" in false_positives[normalized_program]
        is_crosshair_false_positive = normalized_program in false_positives and "crosshair" in false_positives[normalized_program]
        is_nagini_false_positive = normalized_program in false_positives and "nagini" in false_positives[normalized_program]
        
        # Function to convert status with false positive handling
        def get_status(status, is_false_positive):
            if status == "pass":
                return "Pass"
            elif status == "unsupported":
                return "Unsupported"
            elif status == "inconclusive" or (status == "fail" and is_false_positive):
                return "Inconclusive"
            else:
                return "Fail"
        
        verification_results[program_name] = {
            "fuzz_testing": get_status(fuzz_status, is_fuzz_false_positive),
            "crosshair": get_status(crosshair_status, is_crosshair_false_positive),
            "nagini": get_status(nagini_status, is_nagini_false_positive),
            "feq": feq_value
        }
    
    # Create the dataframe with the same structure as before
    data = []
    
    # Map from component names in JSON to the ones used in the original script
    component_map = {
        "params": "param",
        "operations": "op",
        "control_flow": "cf",
        "data_types": "dt",
        "assertions": "assert",
        "math_complexity": "math",
        "loops": "loop",
        "calls": "call",
        "branches": "branch"
    }
    
    # Extract data for each program
    missing_verification = []
    for program in program_data:
        program_name = program["program"]
        difficulty = program["difficulty_score"]
        
        # Get verification results for this program, or use defaults if not found
        if program_name not in verification_results:
            missing_verification.append(program_name)
            verification = {
                "fuzz_testing": "Fail",
                "crosshair": "Fail",
                "nagini": "Fail",
                "feq": 0.5
            }
        else:
            verification = verification_results[program_name]
        
        # Add row to our data with actual verification results
        data.append((
            program_name,
            difficulty,
            verification["fuzz_testing"],
            verification["crosshair"],
            verification["nagini"],
            verification["feq"]
        ))
    
    # Print warning about missing verification results
    if missing_verification:
        print(f"Warning: {len(missing_verification)} programs don't have verification results:")
        for prog in missing_verification:
            print(f"  - {prog}")
            
    # Create DataFrame
    df = pd.DataFrame(
        data,
        columns=["program", "difficulty", "fuzz_testing", "crosshair", "nagini", "feq"],
    )
    
    # Component weights (reusing the original weights)
    component_weights = {
        "param": 0.40,  # Parameter Complexity
        "op": 0.45,  # Operation Density
        "cf": 0.60,  # Control Flow Depth
        "dt": 0.25,  # Data Type Diversity
        "assert": 0.20,  # Assertion Complexity
        "math": 0.55,  # Mathematical Sophistication
        "loop": 0.50,  # Loop Complexity
        "call": 0.40,  # Function Call Density
        "branch": 0.45,  # Branching Complexity
    }
    
    # Program complexity subscores - extract from JSON
    complexity_subscores = {}
    
    for program in program_data:
        program_name = program["program"]
        component_scores = program["component_scores"]
        
        # Map component names and create subscore dictionary for this program
        subscores = {}
        for json_key, orig_key in component_map.items():
            if json_key in component_scores:
                subscores[orig_key] = component_scores[json_key]
            else:
                subscores[orig_key] = 0.0  # Default if missing
                
        complexity_subscores[program_name] = subscores

    return df, component_weights, complexity_subscores


def plot_subscore_verification_relationship(
    df, complexity_subscores, component_weights
):
    """
    Create a better visualization of the relationship between component scores and verification results.
    Uses a more effective binning approach and creates multiple visualizations.
    """
    # Set up the output directory
    graphs_dir = os.path.join(PROJECT_ROOT, "with_graphs_analysis", "program_complexity", "graphs")
    os.makedirs(graphs_dir, exist_ok=True)
    
    # Create a dataframe with all component scores
    component_df = pd.DataFrame()

    # Extract component scores for each program
    for program, scores in complexity_subscores.items():
        program_row = {"program": program}
        program_row.update(scores)
        component_df = pd.concat(
            [component_df, pd.DataFrame([program_row])], ignore_index=True
        )

    # Merge with verification results
    merged_df = pd.merge(
        component_df,
        df[["program", "difficulty", "fuzz_testing", "crosshair", "nagini"]],
        on="program"
    )
    
    # Components to analyze
    components = list(component_weights.keys())
    component_names = {
        "param": "Parameter Complexity",
        "op": "Operation Density",
        "cf": "Control Flow Depth",
        "dt": "Data Type Diversity",
        "assert": "Assertion Complexity",
        "math": "Mathematical Sophistication",
        "loop": "Loop Complexity",
        "call": "Function Call Density",
        "branch": "Branching Complexity",
    }

    # First visualization: Scatter plot matrix for each verification method
    verification_methods = [
        ("fuzz_testing", "Fuzz Testing", "blue"),
        ("crosshair", "CrossHair", "green"),
        ("nagini", "Nagini", "red"),
    ]
    
    output_files = []
    
    # 1. Create heatmap of pass rates by component score bins
    # This is more informative when data is sparse
    for method, method_name, color in verification_methods:
        # Create a figure with 3x3 subplots
        fig, axes = plt.subplots(3, 3, figsize=(15, 15))
        fig.suptitle(f"{method_name} Pass Rate by Component Score", fontsize=16)
        axes = axes.flatten()
        
        for i, component in enumerate(components):
            ax = axes[i]
            
            # Get component values and convert verification to numeric (Pass=1, Fail=0)
            component_values = merged_df[component].values
            
            # Filter out unsupported and inconclusive results
            method_df = merged_df[(merged_df[method] != "Unsupported") & (merged_df[method] != "Inconclusive")].copy()
            method_df[f"{method}_numeric"] = method_df[method].apply(lambda x: 1 if x == "Pass" else 0)
            
            if len(method_df) == 0:
                ax.text(0.5, 0.5, "No supported programs", ha='center', va='center')
                ax.set_title(component_names[component])
                continue
            
            # Determine number of bins based on data distribution
            # More data points = more bins
            unique_values = len(np.unique(method_df[component]))
            n_bins = min(max(3, unique_values // 2), 8)  # Between 3 and 8 bins
            
            # Create bins
            if unique_values > 1:
                bins = np.linspace(method_df[component].min(), method_df[component].max(), n_bins + 1)
                bin_centers = (bins[:-1] + bins[1:]) / 2
                digitized = np.digitize(method_df[component], bins) - 1
                digitized = np.clip(digitized, 0, len(bin_centers) - 1)  # Ensure within bounds
                
                # Calculate pass rate for each bin
                pass_rates = []
                confidence = []  # For confidence interval - based on sample size
                sample_sizes = []
                
                # Skip if we somehow have empty bins
                if len(bin_centers) == 0:
                    ax.text(0.5, 0.5, "Cannot create bins", ha='center', va='center')
                    ax.set_title(component_names[component])
                    continue
                    
                for bin_idx in range(len(bin_centers)):
                    bin_items = method_df[digitized == bin_idx]
                    if len(bin_items) > 0:
                        pass_rate = bin_items[f"{method}_numeric"].mean() * 100
                        pass_rates.append(pass_rate)
                        sample_sizes.append(len(bin_items))
                        # Simple confidence measure: higher with more samples
                        conf = min(1.0, len(bin_items) / 5)  # Max confidence at 5+ samples
                        confidence.append(conf)
                    else:
                        pass_rates.append(0)
                        sample_sizes.append(0)
                        confidence.append(0)
                
                # Create bar chart of pass rates
                bars = ax.bar(bin_centers, pass_rates, width=(bins[1]-bins[0])*0.8, 
                        color=[color if c > 0 else 'gray' for c in confidence], 
                        alpha=0.7)
                
                # Add sample size as text on each bar
                for bar, size, conf in zip(bars, sample_sizes, confidence):
                    # Adjust opacity of text based on confidence
                    text_alpha = max(0.7, conf)
                    if size > 0:
                        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                                str(size), ha='center', va='bottom', fontsize=9, 
                                alpha=text_alpha)
                
                ax.set_ylim(0, 105)
                ax.set_xlabel(f"{component_names[component]} Score Bins")
                ax.set_ylabel("Pass Rate (%)")
                ax.grid(axis='y', alpha=0.3)
            else:
                # Not enough unique values for binning
                pass_rate = method_df[f"{method}_numeric"].mean() * 100
                ax.bar([component_values[0]], [pass_rate], width=0.5, color=color)
                ax.text(component_values[0], pass_rate + 5, 
                        f"n={len(method_df)}", ha='center', va='bottom')
                ax.set_ylim(0, 105)
                ax.set_xlabel(f"{component_names[component]} Score")
                ax.set_ylabel("Pass Rate (%)")
                ax.grid(axis='y', alpha=0.3)
            
            ax.set_title(component_names[component])
        
        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust for suptitle
        output_file = f"{method}_component_pass_rates.png"
        plt.savefig(os.path.join(graphs_dir, output_file), dpi=300)
        plt.close()
        output_files.append(output_file)
    
    # 2. Create scatter plot of pass/fail by overall program difficulty
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("Verification Success by Program Difficulty", fontsize=16)
    
    for i, (method, method_name, color) in enumerate(verification_methods):
        ax = axes[i]
        
        # Filter out unsupported and inconclusive results for Nagini
        method_df = merged_df[(merged_df[method] != "Unsupported") & (merged_df[method] != "Inconclusive")].copy()
        
        if len(method_df) == 0:
            ax.text(0.5, 0.5, "No supported programs", ha='center', va='center')
            ax.set_title(method_name)
            continue
        
        # Split into pass/fail groups
        pass_df = method_df[method_df[method] == "Pass"]
        fail_df = method_df[method_df[method] == "Fail"]
        
        # Create jittered scatter plot
        jitter = 0.1
        ax.scatter(pass_df["difficulty"] + np.random.uniform(-jitter, jitter, size=len(pass_df)), 
                  [1] * len(pass_df), color=color, marker='o', s=50, alpha=0.7, label="Pass")
        ax.scatter(fail_df["difficulty"] + np.random.uniform(-jitter, jitter, size=len(fail_df)), 
                  [0] * len(fail_df), color='gray', marker='x', s=50, alpha=0.7, label="Fail")
        
        # Add a logistic regression curve if enough data points
        if len(pass_df) > 2 and len(fail_df) > 2:
            try:
                # Try to import scikit-learn, but skip if not available
                try:
                    from sklearn.linear_model import LogisticRegression
                    has_sklearn = True
                except ImportError:
                    has_sklearn = False
                
                # Try to import scipy, but skip if not available
                try:
                    from scipy.stats import pointbiserialr
                    has_scipy = True
                except ImportError:
                    has_scipy = False
                
                # Only proceed if scikit-learn is available
                if has_sklearn:
                    X = method_df[["difficulty"]].values
                    y = (method_df[method] == "Pass").astype(int).values
                    
                    model = LogisticRegression(random_state=0)
                    model.fit(X, y)
                    
                    # Create a smooth curve
                    x_range = np.linspace(method_df["difficulty"].min() - 0.5, method_df["difficulty"].max() + 0.5, 100)
                    y_pred = model.predict_proba(x_range.reshape(-1, 1))[:, 1]
                    
                    ax.plot(x_range, y_pred, color=color, linestyle='--', alpha=0.8)
                
                # Calculate and show correlation if scipy is available
                if has_scipy:
                    X_flat = method_df["difficulty"].values
                    y = (method_df[method] == "Pass").astype(int).values
                    correlation, p_value = pointbiserialr(y, X_flat)
                    correlation_text = f"Correlation: {correlation:.2f}"
                    if p_value < 0.05:
                        correlation_text += " (p<0.05)"
                    ax.text(0.05, 0.05, correlation_text, transform=ax.transAxes, 
                           bbox=dict(facecolor='white', alpha=0.8))
            except Exception as e:
                # Log error but continue
                print(f"Warning: Error generating regression for {method_name}: {str(e)}")
        
        # Add counts to legend
        ax.legend(labels=[f"Pass ({len(pass_df)})", f"Fail ({len(fail_df)})"])
        
        ax.set_title(method_name)
        ax.set_xlabel("Program Difficulty Score")
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["Fail", "Pass"])
        ax.set_ylim(-0.5, 1.5)
        ax.grid(alpha=0.3)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    difficulty_file = "verification_by_difficulty.png"
    plt.savefig(os.path.join(graphs_dir, difficulty_file), dpi=300)
    plt.close()
    output_files.append(difficulty_file)
    
    # 3. Create correlation matrix heatmap
    # This shows how each component correlates with verification success
    try:
        plt.figure(figsize=(12, 8))
        
        # Set up correlation matrix
        correlation_data = []
        column_names = []
        
        # Calculate correlations for each verification method with each component
        for method, method_name, _ in verification_methods:
            # Skip nagini if not enough supported programs
            method_df = merged_df[(merged_df[method] != "Unsupported") & (merged_df[method] != "Inconclusive")].copy()
            if method == "nagini" and len(method_df) < 5:
                continue
                
            method_df[f"{method}_numeric"] = method_df[method].apply(lambda x: 1 if x == "Pass" else 0)
            
            method_correlations = []
            for component in components:
                try:
                    if len(np.unique(method_df[component])) > 1:  # Need variation to calculate correlation
                        corr = np.corrcoef(method_df[component], method_df[f"{method}_numeric"])[0, 1]
                        method_correlations.append(corr)
                    else:
                        method_correlations.append(np.nan)
                except Exception:
                    # Handle any correlation calculation errors
                    method_correlations.append(np.nan)
            
            correlation_data.append(method_correlations)
            column_names.append(method_name)
        
        # Only create the heatmap if we have data
        if correlation_data and all(len(row) > 0 for row in correlation_data):
            # Convert to DataFrame
            correlation_df = pd.DataFrame(correlation_data, 
                                        columns=[component_names[c] for c in components],
                                        index=column_names)
            
            # Create heatmap
            sns.heatmap(correlation_df, annot=True, cmap="coolwarm", center=0,
                        vmin=-1, vmax=1, fmt=".2f", linewidths=.5)
            
            plt.title("Correlation between Component Scores and Verification Success")
            plt.tight_layout()
            correlation_file = "component_verification_correlation.png"
            plt.savefig(os.path.join(graphs_dir, correlation_file), dpi=300)
            plt.close()
            output_files.append(correlation_file)
        else:
            print("Warning: Not enough data to create correlation heatmap")
    except Exception as e:
        print(f"Error creating correlation heatmap: {str(e)}")
        # Continue without the heatmap
    
    return output_files


def main():
    # Extract data from JSON instead of LaTeX
    df, component_weights, complexity_subscores = extract_data_from_json()
    
    # Check if data loading was successful
    if df is None or component_weights is None or complexity_subscores is None:
        print("Error: Failed to load required data. Exiting.")
        return

    # Create the visualization
    output_files = plot_subscore_verification_relationship(
        df, complexity_subscores, component_weights
    )

    # Print results
    print("Program Complexity Analysis")
    print("==========================")
    print(f"Total programs analyzed: {len(df)}")
    print(
        f"Complexity distribution: Min={df['difficulty'].min():.2f}, Max={df['difficulty'].max():.2f}, Mean={df['difficulty'].mean():.2f}"
    )

    # Count passing, failing, inconclusive, and unsupported for each method
    fuzz_pass = (df["fuzz_testing"] == "Pass").sum()
    fuzz_fail = (df["fuzz_testing"] == "Fail").sum()
    fuzz_inconclusive = (df["fuzz_testing"] == "Inconclusive").sum()
    
    crosshair_pass = (df["crosshair"] == "Pass").sum()
    crosshair_fail = (df["crosshair"] == "Fail").sum()
    crosshair_inconclusive = (df["crosshair"] == "Inconclusive").sum()
    
    nagini_pass = (df["nagini"] == "Pass").sum()
    nagini_fail = (df["nagini"] == "Fail").sum()
    nagini_inconclusive = (df["nagini"] == "Inconclusive").sum()
    nagini_unsupported = (df["nagini"] == "Unsupported").sum()

    print("\nVerification Pass Counts:")
    fuzz_valid = fuzz_pass + fuzz_fail  # Exclude inconclusive from percentage calculation
    cross_valid = crosshair_pass + crosshair_fail
    nagini_valid = nagini_pass + nagini_fail
    
    print(f"  Fuzz Testing: {fuzz_pass}/{fuzz_valid} ({fuzz_pass / max(1, fuzz_valid) * 100:.1f}%) with {fuzz_inconclusive} inconclusive results")
    print(f"  CrossHair: {crosshair_pass}/{cross_valid} ({crosshair_pass / max(1, cross_valid) * 100:.1f}%) with {crosshair_inconclusive} inconclusive results")
    print(f"  Nagini: {nagini_pass}/{nagini_valid} ({nagini_pass / max(1, nagini_valid) * 100:.1f}%) with {nagini_inconclusive} inconclusive results and {nagini_unsupported} unsupported programs")

    # Calculate correlation between difficulty score and verification success
    df_for_corr = df.copy()
    # Filter out inconclusive results for correlation calculation
    df_for_corr = df_for_corr[(df_for_corr["fuzz_testing"] != "Inconclusive")]
    df_for_corr["fuzz_numeric"] = df_for_corr["fuzz_testing"].apply(lambda x: 1 if x == "Pass" else 0)
    
    df_for_corr = df_for_corr[(df_for_corr["crosshair"] != "Inconclusive")]
    df_for_corr["crosshair_numeric"] = df_for_corr["crosshair"].apply(lambda x: 1 if x == "Pass" else 0)
    
    # Only include "Pass" and "Fail" for Nagini, not "Unsupported" or "Inconclusive"
    nagini_df = df_for_corr[(df_for_corr["nagini"] != "Unsupported") & (df_for_corr["nagini"] != "Inconclusive")].copy()
    nagini_df["nagini_numeric"] = nagini_df["nagini"].apply(lambda x: 1 if x == "Pass" else 0)
    
    print("\nCorrelation with Difficulty Score:")
    if len(df_for_corr) > 1 and "fuzz_numeric" in df_for_corr.columns:
        fuzz_corr = df_for_corr['difficulty'].corr(df_for_corr['fuzz_numeric'])
        print(f"  Fuzz Testing: {fuzz_corr:.4f}")
    else:
        print("  Fuzz Testing: Not enough valid data for correlation")
        
    if len(df_for_corr) > 1 and "crosshair_numeric" in df_for_corr.columns:
        crosshair_corr = df_for_corr['difficulty'].corr(df_for_corr['crosshair_numeric'])
        print(f"  CrossHair: {crosshair_corr:.4f}")
    else:
        print("  CrossHair: Not enough valid data for correlation")
        
    if len(nagini_df) > 1:
        nagini_corr = nagini_df['difficulty'].corr(nagini_df['nagini_numeric'])
        print(f"  Nagini: {nagini_corr:.4f} (based on {len(nagini_df)} supported programs)")
    else:
        print("  Nagini: Not enough valid data for correlation")

    print("\nComplexity Component Weights:")
    sorted_components = sorted(
        component_weights.items(), key=lambda x: x[1], reverse=True
    )
    for component, weight in sorted_components:
        print(f"  {component}: {weight}")

    print(f"\nAnalysis complete. Visualizations saved to: {', '.join(output_files)}")

    # Print correlation table between each component and each method
    print("\nCorrelation Table: Component Scores vs. Verification Outcomes")
    print("=========================================================")
    # Prepare data for correlation table
    methods = [
        ("fuzz_testing", "Fuzz Testing"),
        ("crosshair", "CrossHair"),
        ("nagini", "Nagini"),
    ]
    components = list(component_weights.keys())
    component_names = {
        "param": "Parameter Complexity",
        "op": "Operation Density",
        "cf": "Control Flow Depth",
        "dt": "Data Type Diversity",
        "assert": "Assertion Complexity",
        "math": "Mathematical Sophistication",
        "loop": "Loop Complexity",
        "call": "Function Call Density",
        "branch": "Branching Complexity",
    }
    # Merge component scores with verification results
    component_df = pd.DataFrame()
    for program, scores in complexity_subscores.items():
        program_row = {"program": program}
        program_row.update(scores)
        component_df = pd.concat(
            [component_df, pd.DataFrame([program_row])], ignore_index=True
        )
    merged_df = pd.merge(
        component_df,
        df[["program", "difficulty", "fuzz_testing", "crosshair", "nagini"]],
        on="program"
    )
    # Calculate correlations
    table = []
    for method, method_name in methods:
        # Filter out unsupported and inconclusive
        method_df = merged_df[(merged_df[method] != "Unsupported") & (merged_df[method] != "Inconclusive")].copy()
        method_df[f"{method}_numeric"] = method_df[method].apply(lambda x: 1 if x == "Pass" else 0)
        row = []
        for component in components:
            if len(method_df) > 1 and len(np.unique(method_df[component])) > 1:
                corr = method_df[component].corr(method_df[f"{method}_numeric"])
                row.append(f"{corr:.2f}")
            else:
                row.append("NA")
        table.append((method_name, row))
    # Print header
    header = [component_names[c] for c in components]
    table_lines = []
    table_lines.append(f"{'Method':<12} | " + " | ".join([f"{h:<26}" for h in header]))
    table_lines.append("-" * (13 + 29 * len(header)))
    for method_name, row in table:
        table_lines.append(f"{method_name:<12} | " + " | ".join([f"{v:<26}" for v in row]))
    # Print to console
    for line in table_lines:
        print(line)
    # Save to txt file in graphs_dir
    table_txt_path = os.path.join(PROJECT_ROOT, "with_graphs_analysis", "program_complexity", "graphs", "component_verification_correlation_table.txt")
    with open(table_txt_path, "w") as f:
        for line in table_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
