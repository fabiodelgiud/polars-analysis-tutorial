import polars as pl
import numpy as np
from datetime import datetime, timedelta
import sys

# Helper function to generate dates
def generate_dates(num_days):
    base_date = datetime(2024, 1, 1)
    return [base_date + timedelta(days=x) for x in range(num_days)]

# Create dummy sales data
num_records = 1000
np.random.seed(42)  # For reproducibility

# Generate sample data
data = {
    'date': generate_dates(100) * 10,  # Repeat dates to have multiple sales per day
    'product_id': np.random.randint(1, 6, num_records),
    'product_name': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'], num_records),
    'category': np.random.choice(['Electronics', 'Accessories'], num_records),
    'price': np.random.uniform(100, 2000, num_records).round(2),
    'quantity': np.random.randint(1, 10, num_records),
    'customer_id': np.random.randint(1, 201, num_records),
    'region': np.random.choice(['North', 'South', 'East', 'West'], num_records),
    'satisfaction_score': np.random.randint(1, 6, num_records)
}

# Create Polars DataFrame
df = pl.DataFrame(data)

def print_section(title):
    print("\n" + "="*70)
    print(f"Section: {title}")
    print("="*70)

def run_basic_exploration():
    print_section("1. Basic Data Exploration")
    print("\nFirst few rows:")
    print(df.head())
    print("\nDataFrame Info:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.null_count())

def run_time_series():
    print_section("2. Time Series Analysis")
    daily_sales = df.group_by('date').agg([
        pl.col('price').sum().alias('total_sales'),
        pl.col('quantity').sum().alias('total_units'),
        pl.len().alias('num_transactions')
    ]).sort('date')
    print("\nDaily Sales Summary (first 5 days):")
    print(daily_sales.head())
    daily_sales_ma = daily_sales.with_columns([
        pl.col('total_sales').rolling_mean(window_size=7).alias('sales_7day_ma')
    ])
    print("\n7-Day Moving Average of Sales (first 5 days):")
    print(daily_sales_ma.head())

def run_product_analysis():
    print_section("3. Product Analysis")
    product_metrics = df.group_by(['product_name', 'category']).agg([
        pl.col('price').sum().alias('total_revenue'),
        pl.col('quantity').sum().alias('units_sold'),
        pl.col('satisfaction_score').mean().alias('avg_satisfaction'),
        pl.len().alias('num_sales')
    ]).sort('total_revenue', descending=True)
    print("\nProduct Performance Metrics:")
    print(product_metrics)

def run_customer_segmentation():
    print_section("4. Customer Segmentation")
    customer_segments = df.group_by('customer_id').agg([
        pl.col('price').sum().alias('total_spent'),
        pl.len().alias('num_purchases'),
        pl.col('satisfaction_score').mean().alias('avg_satisfaction')
    ])
    customer_segments = customer_segments.with_columns([
        pl.when(pl.col('total_spent') >= pl.col('total_spent').quantile(0.8))
        .then(pl.lit('High Value'))
        .when(pl.col('total_spent') <= pl.col('total_spent').quantile(0.2))
        .then(pl.lit('Low Value'))
        .otherwise(pl.lit('Medium Value'))
        .alias('customer_segment')
    ])
    print("\nCustomer Segments Summary:")
    print(customer_segments.group_by('customer_segment').agg([
        pl.len().alias('num_customers'),
        pl.col('total_spent').mean().alias('avg_spending'),
        pl.col('num_purchases').mean().alias('avg_purchases')
    ]))

def run_regional_analysis():
    print_section("5. Regional Performance")
    regional_analysis = df.group_by('region').agg([
        pl.col('price').sum().alias('total_revenue'),
        pl.col('quantity').sum().alias('units_sold'),
        pl.col('satisfaction_score').mean().alias('avg_satisfaction'),
        pl.n_unique('customer_id').alias('unique_customers')
    ]).sort('total_revenue', descending=True)
    print("\nRegional Performance Metrics:")
    print(regional_analysis)

def run_advanced_analytics():
    print_section("6. Advanced Analytics")
    product_pairs = df.join(
        df,
        on='customer_id',
        how='inner'
    ).filter(
        pl.col('product_name') != pl.col('product_name_right')
    ).group_by([
        'product_name',
        pl.col('product_name_right').alias('paired_product')
    ]).agg([
        pl.len().alias('pair_count')
    ]).sort('pair_count', descending=True)
    print("\nTop Product Pairs (frequently bought together):")
    print(product_pairs.head())

def run_satisfaction_analysis():
    print_section("7. Satisfaction Analysis")
    satisfaction_by_category = df.group_by([
        'category',
        'satisfaction_score'
    ]).agg([
        pl.len().alias('count')
    ]).pivot(
        values='count',
        index='category',
        on='satisfaction_score'
    ).sort('category')
    print("\nSatisfaction Distribution by Category:")
    print(satisfaction_by_category)

def print_help():
    print("""
Usage: python sales_analysis.py [section_number]
Available sections:
1 - Basic Data Exploration
2 - Time Series Analysis
3 - Product Analysis
4 - Customer Segmentation
5 - Regional Performance
6 - Advanced Analytics
7 - Satisfaction Analysis
all - Run all sections
""")

def main():
    if len(sys.argv) == 1:
        print_help()
        return

    section = sys.argv[1].lower()
    
    if section == 'all':
        run_basic_exploration()
        run_time_series()
        run_product_analysis()
        run_customer_segmentation()
        run_regional_analysis()
        run_advanced_analytics()
        run_satisfaction_analysis()
    elif section == '1':
        run_basic_exploration()
    elif section == '2':
        run_time_series()
    elif section == '3':
        run_product_analysis()
    elif section == '4':
        run_customer_segmentation()
    elif section == '5':
        run_regional_analysis()
    elif section == '6':
        run_advanced_analytics()
    elif section == '7':
        run_satisfaction_analysis()
    else:
        print_help()

if __name__ == "__main__":
    main() 