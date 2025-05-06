import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data from the LaTeX document table in the appendix
# Format: program_name, difficulty, fuzz_testing, crosshair, nagini, feq
data = [
    ("process_data", 4, "Pass", "Fail", "Fail", 0.5),
    ("convert_temperature", 5, "Pass", "Fail", "Fail", 0.7),
    ("calculate_discount", 5, "Pass", "Fail", "Fail", 0.7),
    ("process_complex_number", 6, "Pass", "Pass", "Fail", 0.9),
    ("transform_data", 4, "Pass", "Pass", "Pass", 0.0),
    ("circle_area_diff", 7, "Pass", "Pass", "Fail", 0.4),
    ("triangle_checker", 6, "Pass", "Pass", "Fail", 0.4),
    ("temperature_offset", 5, "Pass", "Pass", "Fail", 0.4),
    ("quadratic_discriminant", 7, "Pass", "Fail", "Fail", 0.7),
    ("vector_norm", 6, "Pass", "Pass", "Fail", 0.4),
    ("hypotenuse_diff", 6, "Pass", "Pass", "Pass", 0.4),
    ("ascii_average", 4, "Pass", "Pass", "Pass", 0.0),
    ("list_balance", 5, "Pass", "Pass", "Fail", 0.4),
    ("odd_sum_validator", 5, "Pass", "Pass", "Pass", 0.0),
    ("string_pattern_score", 4, "Pass", "Pass", "Pass", 0.0),
    ("random_mod_calculator", 4, "Pass", "Fail", "Fail", 0.5),
    ("digit_sum_processor", 5, "Pass", "Fail", "Fail", 0.5),
    ("random_value_adjuster", 5, "Pass", "Fail", "Fail", 0.5),
    ("ceiling_multiplier", 6, "Pass", "Fail", "Fail", 0.5),
    ("factorial_root_calculator", 5, "Pass", "Fail", "Fail", 0.5),
    ("digit_length_scorer", 4, "Pass", "Fail", "Fail", 0.5),
    ("random_double_modulo", 5, "Pass", "Fail", "Fail", 0.5),
    ("modulo_scaler", 6, "Pass", "Fail", "Fail", 0.5),
    ("random_adjustment_calculator", 5, "Pass", "Fail", "Fail", 0.5),
    ("factorial_mod_processor", 4, "Pass", "Fail", "Fail", 0.5),
    ("modular_doubler", 5, "Pass", "Fail", "Fail", 0.5),
    ("ceiling_adjustment_calculator", 6, "Pass", "Fail", "Fail", 0.5),
    ("random_sequence_generator", 5, "Pass", "Fail", "Fail", 0.5),
    ("digit_sum_multiplier", 4, "Pass", "Fail", "Fail", 0.5),
    ("factorial_square_root_mod", 5, "Pass", "Fail", "Fail", 0.5),
    ("decimal_ceiling_adjuster", 6, "Pass", "Fail", "Fail", 0.5),
    ("modular_scaling_calculator", 5, "Pass", "Fail", "Fail", 0.5),
    ("digit_count_processor", 4, "Pass", "Fail", "Fail", 0.5),
    ("random_mod_adjuster", 5, "Pass", "Fail", "Fail", 0.5),
    ("factorial_root_modulo", 6, "Pass", "Fail", "Fail", 0.5),
    ("random_pair_modulo", 5, "Pass", "Fail", "Fail", 0.5),
    ("digit_pair_calculator", 6, "Pass", "Fail", "Fail", 0.5),
    ("modular_multiplication_scaler", 5, "Pass", "Fail", "Fail", 0.5),
    ("float_ceiling_adjuster", 4, "Pass", "Fail", "Fail", 0.5),
    ("factorial_modulo_processor", 5, "Pass", "Fail", "Fail", 0.5),
    ("sum_until_limit", 6, "Pass", "Fail", "Fail", 0.8),
    ("count_divisibles", 5, "Pass", "Pass", "Pass", 0.0),
    ("index_weighted_sum", 5, "Pass", "Fail", "Fail", 0.5),
    ("square_accumulator", 5, "Pass", "Pass", "Pass", 0.0),
    ("rolling_maximum", 6, "Pass", "Pass", "Pass", 0.0),
    ("character_counter", 6, "Pass", "Pass", "Pass", 0.0),
    ("loop_even_sum", 8, "Pass", "Pass", "Fail", 0.4),
    ("loop_string_hash", 5, "Pass", "Pass", "Pass", 0.6),
]

# Convert to DataFrame
df = pd.DataFrame(
    data,
    columns=["program", "difficulty", "fuzz_testing", "crosshair", "nagini", "feq"],
)


# Calculate success rates per complexity level
def calculate_success_rates():
    # Group by difficulty and calculate percentage of passes for each tool
    difficulty_groups = df.groupby("difficulty")

    results = []
    for difficulty, group in difficulty_groups:
        total = len(group)
        fuzz_pass = (group["fuzz_testing"] == "Pass").sum() / total * 100
        crosshair_pass = (group["crosshair"] == "Pass").sum() / total * 100
        nagini_pass = (group["nagini"] == "Pass").sum() / total * 100

        results.append(
            {
                "difficulty": difficulty,
                "fuzz_pass_rate": fuzz_pass,
                "crosshair_pass_rate": crosshair_pass,
                "nagini_pass_rate": nagini_pass,
                "count": total,
            }
        )

    return pd.DataFrame(results)


# Create the complexity vs verification success rate plot
def create_complexity_verification_plot():
    success_rates = calculate_success_rates()

    plt.figure(figsize=(12, 8))

    # Add a little jitter to make overlapping points visible
    jitter = 0.1

    # Fuzz Testing
    plt.scatter(
        success_rates["difficulty"]
        + np.random.uniform(-jitter, jitter, len(success_rates)),
        success_rates["fuzz_pass_rate"],
        s=success_rates["count"]
        * 20,  # Size represents number of programs at that complexity
        alpha=0.7,
        color="blue",
        marker="o",
        label="Fuzz Testing",
    )

    # CrossHair
    plt.scatter(
        success_rates["difficulty"]
        + np.random.uniform(-jitter, jitter, len(success_rates)),
        success_rates["crosshair_pass_rate"],
        s=success_rates["count"] * 20,
        alpha=0.7,
        color="green",
        marker="^",
        label="CrossHair",
    )

    # Nagini
    plt.scatter(
        success_rates["difficulty"]
        + np.random.uniform(-jitter, jitter, len(success_rates)),
        success_rates["nagini_pass_rate"],
        s=success_rates["count"] * 20,
        alpha=0.7,
        color="red",
        marker="s",
        label="Nagini",
    )

    # Add best fit trend lines for each tool
    for tool, color in zip(
        ["fuzz_pass_rate", "crosshair_pass_rate", "nagini_pass_rate"],
        ["blue", "green", "red"],
    ):
        # Only add trend line if there are enough data points
        if len(success_rates) >= 3:
            x = success_rates["difficulty"]
            y = success_rates[tool]

            # Calculate trend line
            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)

            # Add trend line to plot
            x_trend = np.linspace(min(x), max(x), 100)
            plt.plot(x_trend, p(x_trend), linestyle="--", color=color, alpha=0.6)

    # Add annotations for the number of programs at each complexity level
    for _, row in success_rates.iterrows():
        plt.annotate(
            f"n={int(row['count'])}",
            (row["difficulty"], 10),  # Position at the bottom
            ha="center",
            fontsize=8,
            alpha=0.7,
        )

    # Configure plot
    plt.title("Program Complexity vs. Verification Success Rate", fontsize=15)
    plt.xlabel("Program Complexity Rating (1-10)", fontsize=12)
    plt.ylabel("Verification Success Rate (%)", fontsize=12)
    plt.xticks(range(1, 11))
    plt.yticks(range(0, 101, 10))
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(title="Verification Tool")

    # Additional plot showing raw pass/fail outcomes
    plt.figure(figsize=(15, 10))

    # Create a scatter plot of all programs
    plt.subplot(2, 1, 1)

    # For each verification tool, plot a separate row of points
    tools = ["fuzz_testing", "crosshair", "nagini"]
    colors = ["blue", "green", "red"]
    markers = ["o", "^", "s"]

    for i, (tool, color, marker) in enumerate(zip(tools, colors, markers)):
        # Create y positions for each tool (staggered)
        y_positions = np.ones(len(df)) * (i + 1)

        # Plot 'Pass' results
        pass_idx = df[tool] == "Pass"
        plt.scatter(
            df.loc[pass_idx, "difficulty"]
            + np.random.uniform(-0.1, 0.1, sum(pass_idx)),
            y_positions[pass_idx],
            color=color,
            marker=marker,
            s=80,
            alpha=0.7,
            label=f"{tool} - Pass",
        )

        # Plot 'Fail' results with hollow markers
        fail_idx = df[tool] == "Fail"
        plt.scatter(
            df.loc[fail_idx, "difficulty"]
            + np.random.uniform(-0.1, 0.1, sum(fail_idx)),
            y_positions[fail_idx],
            facecolors="none",
            edgecolors=color,
            marker=marker,
            s=80,
            alpha=0.7,
            label=f"{tool} - Fail",
        )

    plt.yticks([1, 2, 3], ["Fuzz Testing", "CrossHair", "Nagini"])
    plt.xlabel("Program Complexity Rating (1-10)")
    plt.title("Verification Outcomes by Tool and Program Complexity", fontsize=15)
    plt.grid(True, linestyle="--", alpha=0.4, axis="x")

    # Add a smaller second subplot showing distribution of program complexities
    plt.subplot(2, 1, 2)
    complexity_counts = df["difficulty"].value_counts().sort_index()
    bars = plt.bar(
        complexity_counts.index, complexity_counts.values, alpha=0.7, color="purple"
    )

    # Add count labels above each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 0.1,
            f"{int(height)}",
            ha="center",
            fontsize=9,
        )

    plt.xlabel("Program Complexity Rating (1-10)")
    plt.ylabel("Number of Programs")
    plt.title("Distribution of Program Complexity")
    plt.xticks(range(1, 11))
    plt.grid(True, linestyle="--", alpha=0.4, axis="y")

    plt.tight_layout()

    # Save both plots
    plt.savefig("complexity_vs_verification_success.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Return success rates for reporting
    return success_rates


if __name__ == "__main__":
    success_rates = create_complexity_verification_plot()
    print("Generated plots successfully!")
    print("\nVerification Success Rates by Complexity:")
    print(success_rates.to_string(index=False))
