from main import df, plt

"""

9 - Desafio de investigacao

• Formule uma pergunta propria que possa ser respondida com as colunas deste dataset.
• Escreva a pergunta antes de executar a analise.
• Utilize Python/pandas para investigar.
• Crie pelo menos uma visualizacao.
• Escreva uma conclusao de no maximo tres frases baseada nos resultados.

"""

# pergunta:
# quais gêneros musicais possuem maior popularidade média no dataset?

# analise
popularidade_genero = ( df.groupby("track_genre")["popularity"] .mean() .sort_values(ascending=False) )
print("10 generos mais populares:\n")
print(popularidade_genero.head(10))

# Gênero	    Popularidade média
# pop-film	    59,28
# k-pop	        56,89
# chill	        53,65
# sad	        52,37
# grunge	    49,59
# indian	    49,53
# anime	        48,77
# emo	        48,12
# sertanejo	    47,86
# pop	        47,57

# visualização em grafico
popularidade_genero.head(10).sort_values().plot(kind="barh")
plt.xlabel("popularidade média")
plt.ylabel("gênero")
plt.title("10 gêneros com maior popularidade média")
plt.show()

# conclusão:
# o gênero pop-film apresentou a maior popularidade média,
# com aproximadamente 59.28
# seguido por k-pop, chill e sad que estão a frento dos 50 pontos
# comparado aos outros do top 10 que estão mais equilibrados entre 47 e 49 pontos