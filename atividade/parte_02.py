from main import df, plt

"""

2 - Qualidade dos dados: valores ausentes

• Descubra quais colunas possuem valores nulos e a quantidade de nulos em cada uma.
• Calcule o percentual de valores nulos por coluna.
• Crie um grafico de barras mostrando somente as colunas que possuem valores ausentes.
• Qual coluna apresenta o maior percentual de ausencia?
• Interpretacao: voce eliminaria automaticamente todas as linhas que possuem algum valor nulo?
Justifique.

"""

nulos = df.isnull().sum()
print("\ncolunas com nulos:")
print(nulos[nulos > 0])
# tres colunas contém nulos e cada uma tem 1 nulo

percentual_nulos = (df.isnull().sum() / len(df)) * 100
print("\npercentual de valores nulos por coluna:")
print(percentual_nulos[percentual_nulos > 0])
# as tres tem o mesmo percentual de nulos 0,0009%

quantidade_nulos = percentual_nulos[percentual_nulos > 0]
quantidade_nulos.plot(kind="bar")
plt.ylabel("rercentual de valores ausentes")
plt.xlabel("coluna")
plt.title("valores ausentes por coluna")
plt.xticks(rotation=45)
plt.show()

# todas apresentam o mesmo mesmo percentual

# eu eliminaria, pq dados nulos não representam nada