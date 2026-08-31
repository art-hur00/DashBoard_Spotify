from main import df

# • Descubra quantos generos diferentes existem em track_genre.

quantidade_generos = df["track_genre"].nunique()

print("\nquantidade de gêneros diferentes:")
print(quantidade_generos)

