from main import df, plt

#• Escolha uma caracteristica musical e investigue se ela parece ter alguma relacao com popularity.
#  Nao confunda correlacao com causalidade.

correlacao = df["danceability"].corr(df["popularity"])

print("\ncorrelação entre danceability e popularity:")
print(round(correlacao, 3))


# gráfico de dispersão

plt.scatter(
    df["danceability"],
    df["popularity"],
    alpha=0.1
)

plt.xlabel("danceability")
plt.ylabel("popularidade")
plt.title("danceability x popularidade")
plt.show()

