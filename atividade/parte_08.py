from main import df

"""

8 - Cacada aos dados estranhos

• Encontre tres registros, valores ou comportamentos que voce considere estranhos, suspeitos ou
interessantes.
• Para cada descoberta, apresente evidencia utilizando codigo, tabela ou grafico.
• Classifique cada caso como: possivel erro, possivel outlier valido ou comportamento interessante.
• Justifique suas classificacoes.

"""

# caso 1

# evidencia:
print("caso 1:")
print("\n")
print(
    df[df[["artists", "album_name", "track_name"]].isnull().any(axis=1)][ ["track_id", "artists", "album_name", "track_name", "duration_ms", "popularity", "track_genre"] ]
)
# classificação: possível erro

# justificativa:
# foi encontrado um registro do gênero k-pop sem artista, álbum e nome da faixa
# além de possuir duration_ms 0

# caso 2

# convertendo ms para minutos
df["duration_min"] = df["duration_ms"] / 60000

# evidencia:
print("\ncaso 2:")
print("\n")
print(
    df[df["duration_min"] > 60][ ["track_name", "artists", "duration_min", "track_genre"] ].sort_values("duration_min", ascending=False).head()
)
# classificação: possível outlier válido

# justificativa:
# apesar dessas musicas serem muito maiores que a duração típica de uma música
# várias delas são registradas como Continuous DJ Mix, então a duração extrema é aceitavel

# caso 3

print("\ncaso 3:")
print("\n")
generos_por_faixa = ( df.groupby("track_id")["track_genre"] .nunique() .sort_values(ascending=False) )
print(generos_por_faixa.head())

# exemplo:
print("\ntem muitas track_ids que aparecem com mais de um gênero\num exemplo:\n")
print(
    df[df["track_id"] == "6S3JlDAGk3uu3NtZbPnuhS"][ ["track_name", "artists", "track_genre"] ]
)
# “Baby Blue - Remastered 2010” do Badfinger, aparece associada a 9 gêneros diferentes

# classificação: comportamento interessante

# justificativa:
# gêneros musicais podem se sobrepor, então uma mesma música pode receber diferentes classificações.
# então tratar cada repetição de track_id como um erro não é viavel