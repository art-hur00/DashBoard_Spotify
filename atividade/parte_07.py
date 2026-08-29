from main import df, plt

"""

7 - Exploracao das caracteristicas musicais

• Escolha duas destas variaveis: danceability, energy, valence, acousticness, instrumentalness ou
tempo.
• Calcule estatisticas descritivas para as variaveis escolhidas.
• Crie pelo menos um histograma ou boxplot para cada variavel.
• Descreva em palavras o que os graficos mostram.

"""

# Média
print(df[["danceability", "energy"]].mean().round(3))
print("\n")
# danceability    0.567
# energy          0.641

# Mediana
print(df[["danceability", "energy"]].median().round(3))
print("\n")
# danceability    0.580
# energy          0.685

# Mínimo
print(df[["danceability", "energy"]].min().round(3))
print("\n")
# danceability    0
# energy          0

# Máximo
print(df[["danceability", "energy"]].max().round(3))
print("\n")
# danceability    0.985
# energy          1

# Desvio-padrão
print(df[["danceability", "energy"]].std().round(3))
# danceability    0.174
# energy          0.252

plt.hist(df["danceability"], bins=20, edgecolor="black")
plt.xlabel("Danceability")
plt.ylabel("Quantidade")
plt.title("Distribuição de Danceability")
plt.show()

# a maior parte das musicas apresenta valores intermediários de danceability entre 0.5 e 0.6
# isso mostra que a base possui muitas musicas moderadamente dançantes