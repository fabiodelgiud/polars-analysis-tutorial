# Polars Data Analysis Tutorial

This project demonstrates various data analysis techniques using Polars, a fast DataFrame library for Python. The script includes several analysis sections:

1. Basic Data Exploration
2. Time Series Analysis
3. Product Analysis
4. Customer Segmentation
5. Regional Performance
6. Advanced Analytics
7. Satisfaction Analysis

## Requirements

- Python 3.9+
- Polars
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fabiodelgiud/polars-analysis-tutorial.git
cd polars-analysis-tutorial
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install polars numpy
```

## Usage

Run the script with a section number to execute specific analyses:

```bash
python sales_analysis.py [section_number]
```

Available options:
- `1`: Basic Data Exploration
- `2`: Time Series Analysis
- `3`: Product Analysis
- `4`: Customer Segmentation
- `5`: Regional Performance
- `6`: Advanced Analytics
- `7`: Satisfaction Analysis
- `all`: Run all sections

Example:
```bash
python sales_analysis.py 4  # Run customer segmentation analysis
python sales_analysis.py all  # Run all analyses
```

## Project Structure

- `sales_analysis.py`: Main script containing all analysis functions
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore rules
- `README.md`: Project documentation

## Contributing

Feel free to submit issues and enhancement requests! 