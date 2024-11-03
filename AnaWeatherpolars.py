import polars as pl

df = pl.read_csv('weather.csv')
print(df)

df = df.with_columns(pl.col('temperature').fill_null(0),
                     pl.col('humidity').fill_null(0))
# print(df.row(5))
# print(df.slice(2, 5))

#  bedre enn 0 er å lage mean og bruke denne
mean_temp = df['temperature'].mean()
print(mean_temp)

df = df.with_columns((pl.col('temperature') - mean_temp).alias('temp-diff'))
print(df)
