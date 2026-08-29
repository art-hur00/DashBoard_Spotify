from main import df, plt

"""

6 - Explicit x Popularidade
• Descubra quantas faixas possuem explicit = True e quantas possuem explicit = False.
• Compare a popularidade media entre os dois grupos.
• Crie uma visualizacao adequada para comunicar essa comparacao.
• Interpretacao: se um grupo apresentar media maior, podemos concluir que conteudo explicito causa
maior popularidade? Por que?

"""

print(df["explicit"].value_counts())
# False 104253 (não explícitas)
# True 9747 (explícitas)

print("\n")
print(df.groupby("explicit")["popularity"].mean().round(2))     # popularidade média
# False    32.94
# True     36.45

# gráfico de comparação
media_explicit = df.groupby("explicit")["popularity"].mean()
media_explicit.plot(kind="bar")
plt.ylabel("popularidade média")
plt.xlabel("conteúdo explicito")
plt.title("popularidade média: explícitas x não explícitas")
plt.xticks(rotation=0)
plt.show()

# acredito que conteúdo explícito não causa maior popularidade
# fatores como gênero musical, artista, período de lançamento e público,
# pode influenciar tanto o uso de conteúdo explícito quanto a popularidade