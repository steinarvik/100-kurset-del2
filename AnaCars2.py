import polars as pl

# Read the CSV data
df = pl.read_csv('sales.csv')

# Calculate and report the percentage of null values
null_sales = df['sales'].is_null().sum() / len(df) * 100
null_profit = df['profit'].is_null().sum() / len(df) * 100
print(f"Null values in sales: {null_sales:.2f}%")
print(f"Null values in profit: {null_profit:.2f}%")

# Fill null values in 'sales' and 'profit' based on user preference
fill_choice = input("Enter 'mean' to fill nulls with the mean or enter a specific value: ")
if fill_choice == 'mean':
    sales_mean = df['sales'].mean()
    profit_mean = df['profit'].mean()
    df = df.with_columns([
        pl.col('sales').fill_null(sales_mean),
        pl.col('profit').fill_null(profit_mean)
    ])
else:
    fill_value = float(fill_choice)
    df = df.with_columns([
        pl.col('sales').fill_null(fill_value),
        pl.col('profit').fill_null(fill_value)
    ])

# Additional calculations and transformations
df = df.with_columns((pl.col('sales') - sales_mean).alias('sales_diff'))
df = df.with_columns(pl.col('order_date').str.slice(5, 2).cast(pl.Int32).alias('month'))

# Display pivot table by month
pivot_df = df.group_by('month').agg(pl.mean('sales').alias('average_sales'))
print(pivot_df)
pivot_df.write_csv('pivot_table.csv')