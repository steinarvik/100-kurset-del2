import polars as pl

df = pl.read_csv("cars.csv")
# print(df.head())

# print(df.describe())

cly_4_df = df.filter(pl.col('cylinders')==4)
print(cly_4_df)

mean_horsepower = df.group_by('cylinders').agg(pl.col('horsepower').mean())
print(mean_horsepower)

cly_4_df.write_csv('cly_4_cars.csv')