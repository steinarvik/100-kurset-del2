import polars as pl

# Read the CSV data
df = pl.read_csv('sales.csv')

# Calculate mean sales and profit (ignoring null values)
sales_mean = df['sales'].mean()
profit_mean = df['profit'].mean()

# Fill null values in 'sales' and 'profit' with their respective means
df = df.with_columns([
    pl.col('sales').fill_null(sales_mean),
    pl.col('profit').fill_null(profit_mean)
])

# Calculate a new column 'sales_diff' which is the difference between 'sales' and the mean sales
df = df.with_columns((pl.col('sales') - sales_mean).alias('sales_diff'))

# Extract the month from 'order_date' and create a new column 'month'
df = df.with_columns(pl.col('order_date').str.slice(5, 2).cast(pl.Int32).alias('month'))

# Print the modified DataFrame
print(df)

# Create a pivot table, grouping by 'month' and calculating the average sales
pivot_df = df.group_by('month').agg(pl.mean('sales').alias('average_sales'))
print(pivot_df)

# Save the pivot table to a CSV file
pivot_df.write_csv('pivot_table.csv')