# Polars Data Analysis Tutorial

This project demonstrates various data analysis techniques using the Polars library in Python. It includes a comprehensive analysis of a dummy sales dataset with multiple sections covering different aspects of data analysis.

## Features

- Basic data exploration
- Time series analysis
- Product performance analysis
- Customer segmentation
- Regional performance analysis
- Advanced analytics (product affinity)
- Satisfaction analysis

## Requirements

- Python 3.9+
- Polars
- NumPy
- Pandas (for comparison)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/polars-analysis-tutorial.git
cd polars-analysis-tutorial
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with different sections:

```bash
# Show help and available options
python sales_analysis.py

# Run a specific section (1-7)
python sales_analysis.py 1    # Basic Data Exploration
python sales_analysis.py 2    # Time Series Analysis
python sales_analysis.py 3    # Product Analysis
python sales_analysis.py 4    # Customer Segmentation
python sales_analysis.py 5    # Regional Performance
python sales_analysis.py 6    # Advanced Analytics
python sales_analysis.py 7    # Satisfaction Analysis

# Run all sections
python sales_analysis.py all
```

## Project Structure

- `sales_analysis.py`: Main script containing all analysis functions
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore rules
- `README.md`: Project documentation

## Contributing

Feel free to submit issues and enhancement requests! 