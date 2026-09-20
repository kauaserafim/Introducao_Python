# -*- coding: utf-8 -*-
import pandas as pd

dados = {
    "Nome": ["Kauã", "Bruna", "Ayumi", "Arthur"],
    "Idade": [19, 18, 7, 12],
    "Comida": ["Churrasco", "Sushi", "Churrasco", "Churrasco"]
}

# converter para a estrutura principal (DataFrame)
df = pd.DataFrame(dados)

# exibir o conteúdo
print(df)

# exibir somente a coluna NOME
print(df["Nome"])

# exibir as colunas NOME e COMIDA
print(df[["Nome", "Comida"]])

# calculos nos Dados
print("Média: ", df["Idade"].mean())
print("Maior idade: ",df["Idade"].max())
print("Menor idade: ",df["Idade"].min())

# filtros de Dados
pessoas = df[df["Idade"] >= 10]
print(pessoas)

menorIdade = df[df["Idade"] <= 10]
print(menorIdade)

# adicionar uma NOVA coluna
df["Situação"] = "Reprovado"
print(df)

# alterar um valor na NOVA coluna
df.loc[df["Idade"] >= 7, "Situação"] = "Aprovado"
print(df)

# ler o arquivo
df_csv = pd.read_csv("dados.csv")

# exibir 5 primeiras linhas
print(df_csv.head())

# exibir 5 últimas linhas
print(df_csv.tail())
