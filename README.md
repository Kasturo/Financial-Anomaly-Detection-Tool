# Financial Fraud Detection Tool — Benford's Law Analyzer

A Python-based diagnostic tool that screens numerical datasets for compliance with **Benford's Law**, a statistical principle widely used in forensic accounting and auditing to flag potentially manipulated or fabricated data.

## How it works

Benford's Law states that in naturally occurring numerical data, smaller digits appear as the leading digit far more often than larger ones. Real-world data like financial transactions, invoice amounts, and expense reports tends to follow this pattern closely. When someone fabricates numbers, they typically distribute digits too evenly or unconsciously favor certain digits — causing the distribution to deviate from what Benford's Law predicts.

This tool computes the first-digit distribution of any Excel dataset and compares it against the expected Benford distribution, flagging deviations that may warrant further investigation.

| Digit | Expected Frequency |
|-------|--------------------|
| 1     | 30.1%              |
| 2     | 17.6%              |
| 3     | 12.5%              |
| 4     | 9.7%               |
| 5     | 7.9%               |
| 6     | 6.7%               |
| 7     | 5.8%               |
| 8     | 5.1%               |
| 9     | 4.6%               |

## Features
- Reads `.xlsx` Excel files using `pandas`
- Filters and processes all numeric columns automatically
- Handles negative numbers correctly
- Computes observed first digit frequencies and compares against Benford's expected distribution
- Prints a formatted deviation table to the terminal
- Visualizes observed vs. expected distribution as a bar chart with overlay curve

## Sample Output
```
Digit   Count   Observed%   Expected%   Deviation
----------------------------------------------------
1       4483    27.86       30.10       -2.24
2       2746    17.06       17.61       -0.54
3       2143    13.32       12.49       +0.82
...
```

## Usage

**Requirements:**
```
pandas
matplotlib
openpyxl
```

Install dependencies:
```bash
pip install pandas matplotlib openpyxl
```

Run the script:
```bash
#Default (looks for "World Population.xlsx" in current directory)
python frequencyAnalyzer.py

# Custom file path
python frequencyAnalyzer.py path/to/your/data.xlsx
```

To use this as a fraud screening tool, swap in a dataset of financial records such as transaction logs, expense reports, or invoice amounts.

## Interpreting Results

- Small deviations (< ±2%) suggest the dataset conforms to Benford's Law and is consistent with naturally occurring data.
- Large deviations on specific digits may indicate manipulation or fabrication of data
- This tool is intended as a first pass screening module,

## Sample Dataset
The included `World_Population.xlsx` (World Bank, 264 countries, 1960–2020) is used as a validation dataset,  population data is a textbook example of Benford conforming data, confirming the tools output is correct before applying it to financial records