import polars as pl
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def print_section(title):
    print("\n" + "="*50)
    print(f"Section: {title}")
    print("="*50)

def section1_basic_operations():
    print_section("1. Basic Operations")
    
    # Create a simple DataFrame
    df = pl.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 75000]
    })
    print("\nOriginal DataFrame:")
    print(df)
    
    # Basic operations
    print("\nBasic operations:")
    print("Mean age:", df['age'].mean())
    print("Max salary:", df['salary'].max())
    
    # Filtering
    print("\nFiltered DataFrame (age > 30):")
    print(df.filter(pl.col('age') > 30))
    
    # Adding a new column
    print("\nDataFrame with new column (bonus):")
    print(df.with_columns(
        (pl.col('salary') * 0.1).alias('bonus')
    ))

def section2_advanced_operations():
    print_section("2. Advanced Operations")
    
    # Create a more complex DataFrame
    dates = [datetime.now() - timedelta(days=x) for x in range(5)]
    df = pl.DataFrame({
        'date': dates,
        'product': ['A', 'B', 'A', 'C', 'B'],
        'quantity': [10, 15, 8, 12, 20],
        'price': [100, 200, 150, 300, 250]
    })
    
    print("\nOriginal DataFrame:")
    print(df)
    
    # Group by operations
    print("\nGroup by product and calculate metrics:")
    print(df.group_by('product').agg([
        pl.col('quantity').sum().alias('total_quantity'),
        pl.col('price').mean().alias('avg_price')
    ]))
    
    # Window functions
    print("\nRunning total of quantity:")
    print(df.with_columns(
        pl.col('quantity').cum_sum().alias('running_total')
    ))

def section3_data_import_export():
    print_section("3. Data Import/Export")
    
    # Create sample data
    df = pl.DataFrame({
        'id': range(1, 6),
        'value': np.random.randn(5),
        'category': ['A', 'B', 'A', 'C', 'B']
    })
    
    # Save to CSV
    df.write_csv('sample_data.csv')
    print("\nData saved to 'sample_data.csv'")
    
    # Read from CSV
    df_read = pl.read_csv('sample_data.csv')
    print("\nData read from CSV:")
    print(df_read)

def section4_comparison_with_pandas():
    print_section("4. Comparison with Pandas")
    
    # Create the same DataFrame in both Polars and Pandas
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'salary': [50000, 60000, 75000]
    }
    
    # Polars DataFrame
    pl_df = pl.DataFrame(data)
    print("\nPolars DataFrame:")
    print(pl_df)
    
    # Pandas DataFrame
    pd_df = pd.DataFrame(data)
    print("\nPandas DataFrame:")
    print(pd_df)
    
    # Compare operations
    print("\nComparison of operations:")
    print("Polars mean:", pl_df['age'].mean())
    print("Pandas mean:", pd_df['age'].mean())

def main():
    print("Welcome to the Polars Tutorial!")
    print("This tutorial will demonstrate various Polars operations.")
    
    # Run each section
    section1_basic_operations()
    section2_advanced_operations()
    section3_data_import_export()
    section4_comparison_with_pandas()
    
    print("\nTutorial completed! Feel free to modify the code and experiment!")

if __name__ == "__main__":
    main() 