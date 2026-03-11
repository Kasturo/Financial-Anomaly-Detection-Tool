import sys
import math
import pandas as pd
import matplotlib.pyplot as plt


# Benford's Law expected probabilities for digits 1-9
BENFORDS_LAW = {i: math.log10(1 + 1 / i) * 100 for i in range(1, 10)}


def extract_first_digits(data: pd.DataFrame) -> dict:
    """Count first digit frequencies across all numeric columns."""
    digit_frequency = {i: 0 for i in range(1, 10)}

    for col in data.columns:
        for val in data[col]:
            if isinstance(val, (int, float)):
                first_dig = str(abs(val))[0]  # abs() handles negatives
                if first_dig.isdigit():
                    first_dig = int(first_dig)
                    if first_dig in digit_frequency:
                        digit_frequency[first_dig] += 1

    return digit_frequency


def compute_percentages(digit_frequency: dict) -> dict:
    """Convert raw counts to percentages."""
    total = sum(digit_frequency.values())
    if total == 0:
        return {i: 0 for i in range(1, 10)}
    return {digit: (count / total) * 100 for digit, count in digit_frequency.items()}


def print_table(digit_frequency: dict, percentages: dict):
    """Print a formatted frequency table with Benford comparison."""
    print(f"\n{'Digit':<8}{'Count':<10}{'Observed %':<14}{'Expected %':<14}{'Deviation'}")
    print("-" * 55)
    for i in range(1, 10):
        observed = percentages[i]
        expected = BENFORDS_LAW[i]
        deviation = observed - expected
        print(f"{i:<8}{digit_frequency[i]:<10}{observed:<14.2f}{expected:<14.2f}{deviation:+.2f}")


def plot_results(percentages: dict, filename: str):
    """Plot observed vs Benford's expected distribution."""
    digits = list(range(1, 10))
    observed = [percentages[i] for i in digits]
    expected = [BENFORDS_LAW[i] for i in digits]
    x = [str(d) for d in digits]

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(x, observed, color='steelblue', alpha=0.7, label='Observed')
    ax.plot(x, expected, color='crimson', marker='o', linewidth=2,
            markersize=6, label="Benford's Law Expected")

    ax.set_title(f"First Digit Distribution vs Benford's Law\n{filename}", fontsize=13)
    ax.set_xlabel("First Digit")
    ax.set_ylabel("Frequency (%)")
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()
    input("Press Enter to exit...")


def analyze(filepath: str):
    """Main analysis pipeline."""
    print(f"Loading: {filepath}")
    data = pd.read_excel(filepath)

    digit_frequency = extract_first_digits(data)
    percentages = compute_percentages(digit_frequency)

    print_table(digit_frequency, percentages)
    plot_results(percentages, filepath)


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "World Population.xlsx"
    analyze(filepath)