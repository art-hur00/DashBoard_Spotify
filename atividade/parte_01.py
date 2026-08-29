from main import df

"""

1 - Reconhecimento do dataset

• Descubra a quantidade de registros e de colunas da base.
• Liste os nomes das colunas.
• Identifique quais variaveis sao numericas e quais sao categoricas/textuais.
• Observe as cinco primeiras linhas e escolha tres variaveis que voce considera interessantes para uma
analise musical. Explique por que.

"""

print("registros e de colunas da base:", df.shape)
# 114.000 registros e 21 colunas

print("\nnome das colunas:\n", df.columns.tolist())
# Unnamed: 0, track_id, artists, album_name, track_name, popularity,
# duration_ms, explicit, danceability, energy, key, loudness, mode,
# speechiness, acousticness, instrumentalness, liveness, valence, tempo,
# time_signature, track_genre

# a coluna unnamed: 0, funciona apenas como um indice da base e não representa uma caractersstica musical

print("\nvariaveis numericas e textuais:")
df.info()
# numericas: popularity, duration_ms, danceability, energy,
# key, loudness, mode, speechiness, acousticness, instrumentalness,
# liveness, valence, tempo, time_signature

# explicit é uma variavel booleana

print("\ncinco primeiras linhas:\n", df.head())
# tres variaveis que considero interessantes são:

# popularity: para saber quais musicas possuem maior indice de popularidade
# energy: representa o nivel de energia percebido na musica e pode ajudar comparar estilos musicais
# valence: relacionada a positividade musical e pode ser usada para saber diferenças entre musicas mais alegres e mais calmas