from main import df, plt

"""

5 - Investigando a duracao das faixas
• Analise estatisticamente a coluna duration_ms.
• Crie um boxplot de duration_ms e identifique possiveis valores extremos.
• Crie uma nova coluna chamada duration_min convertendo milissegundos para minutos.
• Encontre as cinco faixas mais longas e as cinco mais curtas.
• Interpretacao: valores extremos de duracao devem ser removidos automaticamente? Explique.

"""

# criando coluna de duração de ms para minutos
df["duration_min"] = df["duration_ms"] / 60000

# Média
print(df["duration_min"].mean().round())  # 4 min

# Mediana
print(df["duration_min"].median().round())  # 4 min

# Mínimo
print(df["duration_min"].min().round())    # 0 min

# Máximo
print(df["duration_min"].max().round())     # 87 min

# Desvio-padrão
print(df["duration_min"].std().round())     # 2 min

# boxplot
plt.figure(figsize=(6, 5))
plt.boxplot(
    df["duration_min"],
    patch_artist=True,
    boxprops=dict(facecolor="lightblue", edgecolor="black"),
    medianprops=dict(color="red", linewidth=2),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    flierprops=dict(
        marker="o",
        markerfacecolor="lightgreen",
        markersize=5
    )
)
plt.ylabel("Duração (min)", fontsize=12)
plt.title("Boxplot da duração das músicas", fontsize=14)
plt.grid(axis="y", alpha=0.3)
plt.show()
# valores acima de aproximadamente 300.000ms ou entre 5-6 minutos,
# aparecem como outliers no boxplot

# como metade das músicas está concentrada entre aproximadamente 2,9 e 4,4 minutos,
# a caixa fica pequena. Os pontos acima dela são estatisticamente extremos,
# mas não necessariamente erros

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