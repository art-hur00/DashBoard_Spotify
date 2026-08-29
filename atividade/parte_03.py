from main import df

"""

3 - Registros duplicados
• Verifique quantos registros completamente duplicados existem.
• Crie uma copia do DataFrame, remova os registros duplicados e compare a quantidade de linhas antes
e depois.
• Interpretacao: duas faixas com o mesmo track_name necessariamente sao registros duplicados? Que
outras colunas voce verificaria antes de tomar essa decisao?

"""

# remove o indice "Unnamed: 0" que impede que linhas iguais sejam consideradas duplicadas que daria 0 duplicações
df_sem_indice = df.drop(columns=["Unnamed: 0"])
print("quantidade de registros duplicados:", df_sem_indice.duplicated().sum())  # então fica 450 duplicações completas

# removendo duplicações
duplos = df_sem_indice.copy()
duplos_removidos = duplos.drop_duplicates()
print("\nAntes:", len(df_sem_indice))
print("Depois:", len(duplos_removidos))

# duas musicas com o mesmo track_name não seriam exatamente registros duplicados, antes de remover, eu verificaria
# artists, album_name, duration_ms, track_genre e principalmente track_id