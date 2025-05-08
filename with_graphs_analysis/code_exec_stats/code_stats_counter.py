import os
import json
import sys
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Setup project paths
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, PROJECT_ROOT)

# Ensure graphs directory exists
def ensure_graphs_dir() -> str:
    """Create graphs directory if it doesn't exist."""
    graphs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graphs")
    os.makedirs(graphs_dir, exist_ok=True)
    return graphs_dir

def load_program_difficulty_data() -> List[Dict[str, Any]]:
    """Load program difficulty data from JSON file."""
    json_path = os.path.join(PROJECT_ROOT, "difficulty", "program_difficulty_scores.json")
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading program difficulty data: {e}")
        return []

def create_code_stats_visualization() -> Optional[pd.DataFrame]:
    """Create visualizations for code statistics (loop count, function calls, branch count)."""
    # Load the data
    program_data = load_program_difficulty_data()
    
    if not program_data:
        print("No program data found.")
        return None
    
    # Extract code statistics into a DataFrame
    stats_data = []
    for program in program_data:
        program_name = program.get('program', 'Unknown')
        code_stats = program.get('code_stats', {})
        loop_count = code_stats.get('loop_count', 0)
        function_calls = code_stats.get('function_calls', 0)
        branch_count = code_stats.get('branch_count', 0)
        difficulty_score = program.get('difficulty_score', 0)
        bytecode_complexity = program.get('component_scores', {}).get('bytecode_complexity', 0)
        
        stats_data.append({
            'program': program_name,
            'loop_count': loop_count,
            'function_calls': function_calls,
            'branch_count': branch_count,
            'difficulty_score': difficulty_score,
            'bytecode_complexity': bytecode_complexity
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(stats_data)
    
    # Sort by difficulty score
    df = df.sort_values('difficulty_score', ascending=False)
    
    # Create graphs directory
    graphs_dir = ensure_graphs_dir()
    
    # 1. Create bar chart for each code statistic
    create_stat_bar_chart(df, 'loop_count', 'Loop Count by Program', graphs_dir)
    create_stat_bar_chart(df, 'function_calls', 'Function Calls by Program', graphs_dir)
    create_stat_bar_chart(df, 'branch_count', 'Branch Count by Program', graphs_dir)
    
    # 2. Create a stacked bar chart for all code stats
    create_stacked_bar_chart(df, graphs_dir)
    
    # 3. Create scatter plots comparing code stats to difficulty score
    create_difficulty_correlation_charts(df, graphs_dir)
    
    # 4. Create a heatmap of the correlation between metrics
    create_correlation_heatmap(df, graphs_dir)
    
    print(f"Visualization complete. Images saved to: {graphs_dir}")
    return df

def create_stat_bar_chart(df: pd.DataFrame, stat_column: str, title: str, graphs_dir: str) -> None:
    """Create a bar chart for a specific statistic."""
    plt.figure(figsize=(20, 10))
    
    # Sort by the specific statistic for this chart
    sorted_df = df.sort_values(stat_column, ascending=False)
    
    # Generate gradient colors for the bars based on stat value
    counts = sorted_df[stat_column]
    norm = plt.Normalize(vmin=counts.min(), vmax=counts.max())
    cmap = plt.cm.get_cmap('viridis')
    bar_colors = [cmap(norm(value)) for value in counts]
    
    # Create the bar chart
    bars = plt.bar(sorted_df['program'], sorted_df[stat_column], color=bar_colors, alpha=0.7)
    
    # Configure axes
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel(stat_column.replace('_', ' ').title(), fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # Add mean line
    mean_value = sorted_df[stat_column].mean()
    plt.axhline(mean_value, color='red', linestyle='-', alpha=0.6)
    plt.text(
        0, mean_value + 0.1, 
        f"Mean: {mean_value:.2f}", 
        fontsize=10, color='red'
    )
    
    # Ensure proper spacing
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)
    
    # Save figure
    plt.savefig(os.path.join(graphs_dir, f"{stat_column}_by_program.png"), dpi=300, bbox_inches="tight")
    plt.close()

def create_stacked_bar_chart(df: pd.DataFrame, graphs_dir: str) -> None:
    """Create a stacked bar chart showing all code statistics at once."""
    plt.figure(figsize=(20, 10))
    
    # Sort by total complexity (sum of all stats)
    df['total_stats'] = df['loop_count'] + df['function_calls'] + df['branch_count']
    sorted_df = df.sort_values('total_stats', ascending=False)
    
    # Calculate means for each component
    mean_loop_count = sorted_df['loop_count'].mean()
    mean_function_calls = sorted_df['function_calls'].mean()
    mean_branch_count = sorted_df['branch_count'].mean()
    mean_total = mean_loop_count + mean_function_calls + mean_branch_count
    
    # Create stacked bar
    plt.bar(sorted_df['program'], sorted_df['loop_count'], label='Loop Count', alpha=0.7, color='#1f77b4')
    plt.bar(sorted_df['program'], sorted_df['function_calls'], bottom=sorted_df['loop_count'], 
            label='Function Calls', alpha=0.7, color='#ff7f0e')
    plt.bar(sorted_df['program'], sorted_df['branch_count'], 
            bottom=sorted_df['loop_count'] + sorted_df['function_calls'], 
            label='Branch Count', alpha=0.7, color='#2ca02c')
    
    # Configure axes
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel('Count', fontsize=12)
    plt.title('Code Complexity Metrics by Program', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # Add legend
    legend = plt.legend(loc='upper right', frameon=True)
    
    # Add text box with mean values
    mean_text = (
        f"Mean Values:\n"
        f"Loop Count: {mean_loop_count:.2f}\n"
        f"Function Calls: {mean_function_calls:.2f}\n"
        f"Branch Count: {mean_branch_count:.2f}\n"
        f"Total Mean: {mean_total:.2f}"
    )
    
    # Position the text box below the legend
    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    plt.annotate(mean_text, xy=(0.95, 0.85), xycoords='axes fraction', 
                 fontsize=10, ha='right', va='top', bbox=props)
    
    # Ensure proper spacing
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.3)
    
    # Save figure
    plt.savefig(os.path.join(graphs_dir, "stacked_code_stats.png"), dpi=300, bbox_inches="tight")
    plt.close()

def create_difficulty_correlation_charts(df: pd.DataFrame, graphs_dir: str) -> None:
    """Create scatter plots comparing code statistics to difficulty score."""
    # Prepare data for the scatter plots
    stats_columns = ['loop_count', 'function_calls', 'branch_count']
    
    # Create a single figure with subplots
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    
    for i, stat in enumerate(stats_columns):
        ax = axes[i]
        
        # Create scatter plot
        scatter = ax.scatter(df[stat], df['difficulty_score'], 
                             c=df['bytecode_complexity'], cmap='viridis', 
                             alpha=0.7, s=50)
        
        # Add regression line
        if len(df) > 1:  # Need at least 2 points for regression
            z = np.polyfit(df[stat], df['difficulty_score'], 1)
            p = np.poly1d(z)
            ax.plot(sorted(df[stat]), p(sorted(df[stat])), "r--", alpha=0.7)
            
            # Add correlation coefficient
            corr = df[stat].corr(df['difficulty_score'])
            ax.text(0.05, 0.95, f"Correlation: {corr:.2f}", transform=ax.transAxes, 
                    fontsize=10, verticalalignment='top')
        
        # Configure axes
        ax.set_xlabel(stat.replace('_', ' ').title())
        ax.set_ylabel('Difficulty Score')
        ax.set_title(f'{stat.replace("_", " ").title()} vs Difficulty')
        ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add a colorbar
    cbar = fig.colorbar(scatter, ax=axes, orientation='horizontal', pad=0.05)
    cbar.set_label('Bytecode Complexity')
    
    plt.tight_layout()
    
    # Save figure
    plt.savefig(os.path.join(graphs_dir, "stats_difficulty_correlation.png"), dpi=300)
    plt.close()

def create_correlation_heatmap(df: pd.DataFrame, graphs_dir: str) -> None:
    """Create a heatmap showing correlations between different metrics."""
    # Select columns for correlation
    corr_columns = ['loop_count', 'function_calls', 'branch_count', 
                    'difficulty_score', 'bytecode_complexity']
    
    # Calculate correlation
    corr_matrix = df[corr_columns].corr()
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
                linewidths=0.5, fmt='.2f')
    
    plt.title('Correlation Between Code Statistics and Complexity Metrics')
    plt.tight_layout()
    
    # Save figure
    plt.savefig(os.path.join(graphs_dir, "code_stats_correlation_heatmap.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    df = create_code_stats_visualization()
    if df is not None:
        # Calculate and print summary statistics
        print("\nSummary Statistics:")
        print(f"Total programs analyzed: {len(df)}")
        print("\nLoop Count Statistics:")
        print(f"  Mean: {df['loop_count'].mean():.2f}")
        print(f"  Max: {df['loop_count'].max()} ({df.loc[df['loop_count'].idxmax(), 'program']})")
        
        print("\nFunction Calls Statistics:")
        print(f"  Mean: {df['function_calls'].mean():.2f}")
        print(f"  Max: {df['function_calls'].max()} ({df.loc[df['function_calls'].idxmax(), 'program']})")
        
        print("\nBranch Count Statistics:")
        print(f"  Mean: {df['branch_count'].mean():.2f}")
        print(f"  Max: {df['branch_count'].max()} ({df.loc[df['branch_count'].idxmax(), 'program']})")
    else:
        print("Failed to create visualizations.")
