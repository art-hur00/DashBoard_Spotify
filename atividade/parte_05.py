from main import df, plt

"""

5 - Investigando a duracao das faixas
• Analise estatisticamente a coluna duration_ms.
• Crie um boxplot de duration_ms e identifique possiveis valores extremos.
• Crie uma nova coluna chamada duration_min convertendo milissegundos para minutos.
• Encontre as cinco faixas mais longas e as cinco mais curtas.
• Interpretacao: valores extremos de duracao devem ser removidos automaticamente? Explique.

"""

# Média
print(df["duration_ms"].mean().round())  # 228.029ms

# Mediana
print(df["duration_ms"].median().round())  # 212.906ms

# Mínimo
print(df["duration_ms"].min().round())    # 0ms

# Máximo
print(df["duration_ms"].max().round())     # 5.237.295ms

# Desvio-padrão
print(df["duration_ms"].std().round())     # 107.298ms

# boxplot
plt.boxplot(df["duration_ms"])
plt.ylabel("duração (ms)")
plt.title("boxplot da duração das musicas")
plt.show()
# valores acima de aproximadamente 300.000ms ou entre 5-6 minutos,
# aparecem como outliers no boxplot

# criando coluna de duração de ms para minutos
df["duration_min"] = df["duration_ms"] / 60000

# 5 faixas mais longas
print(
    "\n",
    df.nlargest(5, "duration_ms")[["track_name", "artists", "duration_min", "track_genre"]]
)

# 5 faixas mais curtas
print(
    "\n",
    df.nsmallest(5, "duration_ms")[["track_name", "artists", "duration_min", "track_genre"]]
)
# valores de duração não devem ser removidos pq as músicas mais longas são principalmente remixes que geralmente tem duração maior
# já os registros com duração 0 e ausência de nome e artista pode ser um problema na coleta dos dados