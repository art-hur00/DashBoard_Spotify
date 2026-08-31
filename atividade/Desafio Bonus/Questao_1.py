from main import df

#• Encontre a faixa de maior popularity e mostre seu nome, artista e genero.


maior_popularidade = df["popularity"].max()

faixas_top = df[
    df["popularity"] == maior_popularidade
]

faixa_mais_popular = (
    faixas_top
    .groupby(["track_name", "artists", "popularity"])["track_genre"]
    .unique()
    .reset_index()
)

print("faixa com maior popularidade:")
print(faixa_mais_popular)


