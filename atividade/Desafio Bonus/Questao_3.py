from main import df

# • Encontre os cinco generos com maior quantidade de registros.


generos = df["track_genre"].value_counts()

print("\ncinco primeiros gêneros retornados:")
print(generos.head(5))

print("\nmaior quantidade de registros por gênero:")
print(generos.max())

print("\nquantidade de gêneros com essa mesma quantidade:")
print((generos == generos.max()).sum())

