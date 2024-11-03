import polars as pl
import matplotlib.pyplot as plt

from pythonProject.AnaCars2 import profit_mean

# Read the CSV data
df = pl.read_csv('sales.csv')

# Fill null values in 'sales' and 'profit' with their means
sales_mean = df['sales'].mean()
profit_mean = df['profit'].mean()
df = df.with_columns([
    pl.col('sales').fill_null(sales_mean),
    pl.col('profit').fill_null(profit_mean)
])

# Extract month and calculate monthly averages for the pivot table
df = df.with_columns(pl.col('order_date').str.slice(5, 2).cast(pl.Int32).alias('month'))
pivot_df = df.group_by('month').agg(pl.mean('sales').alias('average_sales'))

# Plot monthly average sales using Matplotlib
pivot_df_pd = pivot_df.to_pandas()  # Convert Polars DataFrame to Pandas for plotting
plt.figure(figsize=(10, 5))
plt.plot(pivot_df_pd['month'], pivot_df_pd['average_sales'], marker='o', color='b')
plt.title("Average Sales by Month")
plt.xlabel("Month")
plt.ylabel("Average Sales")
plt.grid()
plt.show()

# Save pivot table to CSV
pivot_df.write_csv('pivot_table.csv')