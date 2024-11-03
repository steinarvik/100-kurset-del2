import polars as pl

# Load the dataset
df = pl.read_csv('iris.csv')

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Describe the dataset to get summary statistics
print("\nSummary statistics:")
print(df.describe())

# Filter the dataset for a specific species
setosa_df = df.filter(pl.col('species') == 'setosa')
print("\nSetosa species dataset:")
print(setosa_df)

# Group by species and calculate mean of sepal_length
mean_sepal_length = df.groupby('species').agg(pl.col('sepal_length').mean())
print("\nMean sepal length by species:")
print(mean_sepal_length)

# Save the filtered dataframe to a new CSV file
setosa_df.write_csv('setosa_iris.csv')