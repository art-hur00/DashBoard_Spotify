from main import df, plt

"""

4 - Investigando a popularidade
• Utilizando popularity, calcule media, mediana, minimo, maximo e desvio-padrao.
• Crie um histograma da popularidade.
• Crie um boxplot da popularidade.
• Escreva duas observacoes sobre a distribuicao encontrada.
• Interpretacao: uma musica com popularity = 0 significa necessariamente que ela nunca foi ouvida?

"""

# Média
print(df["popularity"].mean().round(2))  # 33.24

# Mediana
print(df["popularity"].median())  # 35

# Mínimo
print(df["popularity"].min())    # 0

# Máximo
print(df["popularity"].max())     # 100

# Desvio-padrão
print(df["popularity"].std().round(2))     # 22.31

# barras
plt.hist(df["popularity"], bins=20, edgecolor="black")
plt.xlabel("popularidade")
plt.ylabel("quantidade de músicas")
plt.title("distribuição da popularidade")
plt.show()

# boxplot
plt.boxplot(df["popularity"])
plt.ylabel("popularidade")
plt.title("boxplot da popularidade")
plt.show()

# observação:
# metade central das musicas possui mais ou menos uma popularidade entre 17 e 50,
# existe uma concentração bastante relevante de popularidade 0, perto de 2.000

# uma musica com popularidade 0 não significa que ela nunca foi ouvida
# esse coluna representa o valor de popularidade registrado na base de dados