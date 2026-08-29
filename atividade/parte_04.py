from main import df, plt

"""

4 - Investigando a popularidade
• Utilizando popularity, calcule media, mediana, minimo, maximo e desvio-padrao.
• Crie um histograma da popularidade.
• Crie um boxplot da popularidade.
• Escreva duas observacoes sobre a distribuicao encontrada.
• Interpretacao: uma musica com popularity = 0 significa necessariamente que ela nunca foi ouvida?

"""

print(df["popularity"].describe())
# Média	            33,23
# Mediana	        35
# Mínimo	        0
# Máximo	        100
# Desvio-padrão	    22,30

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