import ast
import dis
import inspect
import textwrap
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

# Ensure graphs directory exists
def ensure_graphs_dir():
    """Create graphs directory if it doesn't exist."""
    graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphs")
    os.makedirs(graphs_dir, exist_ok=True)
    return graphs_dir


def analyze_file(file_path):
    """Analyze a Python file for computational load between early comment and final assertion."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    functions_data = {}
    current_function = None
    # Stores lines with original indent for the current func's body, after the 'def' line
    function_body_for_current_func = [] 
    early_line_idx_in_body = None
    final_assert_idx_in_body = None
    in_function_scope = False # True if we are inside a def's scope (after the 'def' line)

    # Parse the file line by line
    for i, file_line_with_nl in enumerate(lines):
        line_content_orig_indent = file_line_with_nl.rstrip('\\n')
        line_content_stripped = line_content_orig_indent.strip()

        # Check for function definition
        if line_content_stripped.startswith("def ") and "(" in line_content_stripped:
            # Process previous function if there was one
            if (
                current_function
                and early_line_idx_in_body is not None
                and final_assert_idx_in_body is not None
            ):
                start_slice = early_line_idx_in_body + 1
                end_slice = final_assert_idx_in_body
                # Ensure slice indices are valid
                if 0 <= start_slice <= end_slice <= len(function_body_for_current_func):
                    between_code_with_indent = function_body_for_current_func[start_slice : end_slice]
                else:
                    between_code_with_indent = []
                    print(f"Warning: Indexing issue for {current_function} during processing. EBI: {early_line_idx_in_body}, FAI: {final_assert_idx_in_body}, Len: {len(function_body_for_current_func)}")


                functions_data[current_function] = {
                    "name": current_function, # Added function name
                    "early_comment": early_line_idx_in_body,
                    "final_assert": final_assert_idx_in_body,
                    "between_code": between_code_with_indent, # Has original indent
                    "loc": len(between_code_with_indent),
                    "instruction_count": 0,
                }
                # Count bytecode instructions
                count_bytecode_instructions(
                    functions_data[current_function], between_code_with_indent
                )

            # Start new function
            func_name = line_content_stripped[4 : line_content_stripped.index("(")].strip()
            current_function = func_name
            function_body_for_current_func = [] # Reset for new function's body lines
            early_line_idx_in_body = None
            final_assert_idx_in_body = None
            in_function_scope = True # We are now processing lines for this function's body

        elif in_function_scope: # If we're inside a function's scope (i.e., after its 'def' line)
            # Add the line (with its original indentation) to the current function's body list
            function_body_for_current_func.append(line_content_orig_indent)
            
            # Relative line index within function_body_for_current_func
            rel_line_idx = len(function_body_for_current_func) - 1

            # Check for early assert comment (in the line with original indent)
            if "# Early Assert HERE" in line_content_orig_indent:
                early_line_idx_in_body = rel_line_idx

            # Check for final assertion (check stripped line for assert keyword)
            if line_content_stripped.startswith("assert "):
                final_assert_idx_in_body = rel_line_idx
            
            # Note: End of function is primarily detected by the start of a new 'def' 
            # or EOF (handled by post-loop processing).

    # Process the last function if needed (after loop finishes)
    if (
        current_function
        and early_line_idx_in_body is not None
        and final_assert_idx_in_body is not None
    ):
        start_slice = early_line_idx_in_body + 1
        end_slice = final_assert_idx_in_body
        if 0 <= start_slice <= end_slice <= len(function_body_for_current_func):
            between_code_with_indent = function_body_for_current_func[start_slice : end_slice]
        else:
            between_code_with_indent = []
            print(f"Warning: Indexing issue for {current_function} (post-loop). EBI: {early_line_idx_in_body}, FAI: {final_assert_idx_in_body}, Len: {len(function_body_for_current_func)}")


        functions_data[current_function] = {
            "name": current_function, # Added function name
            "early_comment": early_line_idx_in_body,
            "final_assert": final_assert_idx_in_body,
            "between_code": between_code_with_indent, # Has original indent
            "loc": len(between_code_with_indent),
            "instruction_count": 0,
        }
        # Count bytecode instructions
        count_bytecode_instructions(functions_data[current_function], between_code_with_indent)

    return functions_data


def create_comparative_visualizations(data):
    """Create visualizations comparing computational overhead between assertions."""
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame.from_dict(data, orient="index")

    # Filter out functions without both early comment and final assertion
    df = df[df["early_comment"].notna() & df["final_assert"].notna()]

    # Sort by instruction count
    df = df.sort_values("instruction_count", ascending=False)

    # Create visualizations
    create_bar_chart(df)
    create_scatter_plot(df)
    create_bytecode_density_plot(df)

    return df


def create_bar_chart(df):
    """Create a bar chart of bytecode instruction counts."""
    if plt is None:
        print("Cannot create bar chart: matplotlib not installed")
        return
        
    plt.figure(figsize=(12, 8))

    # Limit to top 25 functions for readability
    if len(df) > 25:
        df_plot = df.head(25)
    else:
        df_plot = df

    plt.bar(df_plot.index, df_plot["instruction_count"], color="#1f77b4")
    plt.xticks(rotation=90)
    plt.xlabel("Function")
    plt.ylabel("Bytecode Instruction Count")
    plt.title(
        "Computational Overhead Between Early and Final Assertions (Bytecode Instructions)"
    )
    plt.tight_layout()
    
    # Save to graphs directory
    graphs_dir = ensure_graphs_dir()
    plt.savefig(os.path.join(graphs_dir, "bytecode_instructions.png"), dpi=300)
    plt.close()


def create_scatter_plot(df):
    """Create a scatter plot comparing instruction count to lines of code."""
    if plt is None or np is None:
        print("Cannot create scatter plot: required libraries not installed")
        return
        
    plt.figure(figsize=(12, 8))

    # Create scatter plot
    plt.scatter(df["loc"], df["instruction_count"], s=80, alpha=0.7)

    # Add labels for each point (limit to 25 for readability)
    df_labeled = df.head(25) if len(df) > 25 else df
    for i, func in enumerate(df_labeled.index):
        plt.annotate(
            func,
            (df_labeled["loc"].iloc[i], df_labeled["instruction_count"].iloc[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
        )

    # Add trend line
    z = np.polyfit(df["loc"], df["instruction_count"], 1)
    p = np.poly1d(z)
    plt.plot(df["loc"], p(df["loc"]), "r--", alpha=0.8)

    # Add correlation coefficient
    corr = df["loc"].corr(df["instruction_count"])
    plt.text(
        0.05,
        0.95,
        f"Correlation: {corr:.2f}",
        transform=plt.gca().transAxes,
        fontsize=10,
        bbox=dict(facecolor="white", alpha=0.8),
    )

    plt.xlabel("Lines of Code")
    plt.ylabel("Bytecode Instruction Count")
    plt.title("Relationship Between Code Size and Computational Overhead")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    # Save to graphs directory
    graphs_dir = ensure_graphs_dir()
    plt.savefig(os.path.join(graphs_dir, "loc_vs_instructions.png"), dpi=300)
    plt.close()


def create_bytecode_density_plot(df):
    """Create a density plot showing bytecode instructions per line of code."""
    if plt is None:
        print("Cannot create density plot: matplotlib not installed")
        return
        
    # Calculate density (instructions per line)
    df["instruction_density"] = df["instruction_count"] / df["loc"].apply(
        lambda x: max(x, 1)
    )

    plt.figure(figsize=(12, 8))

    # Sort by density
    df_sorted = df.sort_values("instruction_density", ascending=False)

    # Limit to top 25 functions for readability
    if len(df_sorted) > 25:
        df_plot = df_sorted.head(25)
    else:
        df_plot = df_sorted

    # Create bar chart
    bars = plt.bar(df_plot.index, df_plot["instruction_density"], color="#2ca02c")

    # Add value annotations
    for i, bar in enumerate(bars):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            f"{df_plot['instruction_density'].iloc[i]:.1f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.xticks(rotation=90)
    plt.xlabel("Function")
    plt.ylabel("Bytecode Instructions per Line of Code")
    plt.title("Computational Density Between Assertions")
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    # Save to graphs directory
    graphs_dir = ensure_graphs_dir()
    plt.savefig(os.path.join(graphs_dir, "bytecode_density.png"), dpi=300)
    plt.close()


def function_categories(df):
    """Categorize functions based on their characteristics for further analysis."""
    if plt is None:
        print("Cannot create categories visualization: matplotlib not installed")
        return {}
        
    categories = {
        "arithmetic": [],
        "string_processing": [],
        "list_processing": [],
        "loop_heavy": [],
        "control_flow": [],
    }

    # This is a simplified categorization based on function names
    # In a real implementation, you might analyze the AST more thoroughly
    for func in df.index:
        if any(
            term in func.lower()
            for term in [
                "sum",
                "calculator",
                "calculate",
                "discount",
                "quadratic",
                "acc",
            ]
        ):
            categories["arithmetic"].append(func)
        elif any(
            term in func.lower()
            for term in ["str", "string", "character", "ascii", "hash"]
        ):
            categories["string_processing"].append(func)
        elif any(
            term in func.lower() for term in ["list", "lst", "array", "nums", "values"]
        ):
            categories["list_processing"].append(func)
        elif any(
            term in func.lower()
            for term in ["loop", "nested", "iterator", "fibonacci", "counter"]
        ):
            categories["loop_heavy"].append(func)
        elif any(
            term in func.lower() for term in ["checker", "validator", "if", "triangle"]
        ):
            categories["control_flow"].append(func)

    # Create a category visualization
    plt.figure(figsize=(12, 8))

    # Collect data
    category_names = list(categories.keys())
    category_counts = [len(categories[cat]) for cat in category_names]
    category_instr_avg = []

    for cat in category_names:
        if categories[cat]:
            funcs = categories[cat]
            avg = df.loc[funcs, "instruction_count"].mean()
            category_instr_avg.append(avg)
        else:
            category_instr_avg.append(0)

    # Create the plot with dual axis
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Plot function counts
    color = "tab:blue"
    ax1.set_xlabel("Function Category")
    ax1.set_ylabel("Number of Functions", color=color)
    bars = ax1.bar(category_names, category_counts, color=color, alpha=0.6)
    ax1.tick_params(axis="y", labelcolor=color)

    # Add count labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{int(height)}",
            ha="center",
            va="bottom",
            color=color,
            fontweight="bold",
        )

    # Create a second y-axis
    ax2 = ax1.twinx()
    color = "tab:red"
    ax2.set_ylabel("Average Instruction Count", color=color)
    ax2.plot(
        category_names, category_instr_avg, "o-", color=color, linewidth=2, markersize=8
    )
    ax2.tick_params(axis="y", labelcolor=color)

    # Add average labels
    for i, v in enumerate(category_instr_avg):
        ax2.text(i, v + 1, f"{v:.1f}", ha="center", color=color, fontweight="bold")

    fig.tight_layout()
    plt.title("Function Categories and Their Computational Overhead")
    
    # Save to graphs directory
    graphs_dir = ensure_graphs_dir()
    plt.savefig(os.path.join(graphs_dir, "function_categories.png"), dpi=300)
    plt.close()

    return categories


def generate_latex_table(df):
    """Generate a LaTeX table for the paper."""
    # Round numeric columns to 2 decimal places
    df_rounded = df.round(2)

    # Select relevant columns
    df_table = df_rounded[["instruction_count", "loc", "instruction_density"]]

    # Rename columns for better readability
    df_table = df_table.rename(
        columns={
            "instruction_count": "Bytecode Instructions",
            "loc": "Lines of Code",
            "instruction_density": "Instructions per Line",
        }
    )

    # Generate LaTeX table manually
    columns = list(df_table.columns)
    rows = df_table.index

    # Start building the LaTeX table
    latex_table = "\\begin{table}[h]\n\\centering\n\\begin{tabular}{|l|"

    # Add column specifications
    for _ in columns:
        latex_table += "r|"
    latex_table += "}\n\\hline\n"

    # Add header row
    latex_table += "Function & " + " & ".join(columns) + " \\\\\n\\hline\n"

    # Add data rows (limit to 25 for space)
    rows_to_show = list(rows)[:25] if len(rows) > 25 else rows
    for row in rows_to_show:
        latex_table += (
            row
            + " & "
            + " & ".join([str(df_table.loc[row, col]) for col in columns])
            + " \\\\\n"
        )

    # Close the table
    latex_table += "\\hline\n\\end{tabular}\n"
    latex_table += "\\caption{Computational Overhead Between Early and Final Assertions (Top 25 Functions)}\n"
    latex_table += "\\label{tab:computational_overhead}\n"
    latex_table += "\\end{table}"

    # Save to file
    graphs_dir = ensure_graphs_dir()
    with open(os.path.join(graphs_dir, "computational_overhead_table.tex"), "w") as f:
        f.write(latex_table)

    return latex_table


def count_bytecode_instructions(function_data, code_lines_with_orig_indent):
    """Count bytecode instructions for code between assertions."""
    if not code_lines_with_orig_indent:
        function_data["instruction_count"] = 0
        return

    # Join lines, which already have their correct relative indentation.
    code_str_orig_indent = "\n".join(code_lines_with_orig_indent)
    
    # Dedent the block to make it suitable for insertion into the temp function.
    # This removes common leading whitespace.
    dedented_code_block = textwrap.dedent(code_str_orig_indent)

    # Now, indent this dedented block for the temp function body.
    # If the dedented block is empty or just whitespace, use 'pass'.
    if not dedented_code_block.strip():
        func_body_for_exec = "    pass"
    else:
        func_body_for_exec = textwrap.indent(dedented_code_block, "    ")
        # Fallback if indent results in effectively empty string (e.g. if dedented_code_block was only newlines)
        if not func_body_for_exec.strip():
            func_body_for_exec = "    pass"
    
    func_name_for_error = function_data.get("name", "Unknown")
    # The final 'pass' ensures the function is valid even if func_body_for_exec 
    # represents an incomplete snippet (e.g. an if without an else).
    func_str = f"def _temp_function():\n{func_body_for_exec}\n    pass"

    try:
        # Compile and load the function
        namespace = {}
        exec(func_str, namespace)
        temp_func = namespace["_temp_function"]

        # Count bytecode instructions
        instruction_count = 0
        bytecode = dis.Bytecode(temp_func)
        for instr in bytecode:
            # Count each actual instruction (skip line numbers, etc.)
            if instr.opcode != dis.opmap.get("EXTENDED_ARG", -1):
                instruction_count += 1

        function_data["instruction_count"] = instruction_count
    except Exception as e:
        # Fallback: estimate based on how many lines we have, with a multiplier
        print(
            f"Warning: Couldn't analyze bytecode for function '{func_name_for_error}', falling back to LOC*3. "
            f"Error: {str(e)}. Snippet (dedented): '''{dedented_code_block[:100].strip()}...'''"
        )
        function_data["instruction_count"] = len(code_lines_with_orig_indent) * 3  # Rough estimate
    return # Explicit return to be clear


def main():
    file_path = os.path.join(PROJECT_ROOT, "code_files", "a_original_programs", "functions.py")
        
    functions_data = analyze_file(file_path)

    # Create visualizations
    df = create_comparative_visualizations(functions_data)

    # Calculate instruction density
    df["instruction_density"] = df["instruction_count"] / df["loc"].apply(
        lambda x: max(x, 1)
    )

    # Analyze function categories
    categories = function_categories(df)

    # Generate LaTeX table
    latex_table = generate_latex_table(df)

    print(
        f"Analysis complete. Found {len(df)} functions with both early comment and final assertion."
    )
    print("Visualizations and LaTeX table have been generated in the 'graphs' directory.")

    # Display summary statistics
    print("\nSummary Statistics:")
    print(df[["instruction_count", "loc", "instruction_density"]].describe())

    # List functions by instruction count (top 25 if there are many)
    print("\nFunctions Ranked by Computational Overhead (Bytecode Instructions):")
    count = 0
    for func, instr_count in df["instruction_count"].items():
        print(f"{func}: {instr_count:.0f} instructions")
        count += 1
        if count >= 25:
            print(
                f"... and {len(df) - 25} more functions (showing top 25 of {len(df)})"
            )
            break


if __name__ == "__main__":
    main()
