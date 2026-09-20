# -*- coding: utf-8 -*-
import pandas as pd

from google.colab import files
files.upload()

df = pd.read_csv("clientes_credito_preparacao_ml.csv")

df.head(20)

# Conhecendo os dados

# Quantidade de registros
# Tipos das colunas
# Valores faltantes
# Valores minímos, máximos e categóricos

df.info()

df.describe(include="all")

df.isnull().sum()

# Categorias inconsistentes
df["estado_civil"].value_counts()

# Valores suspeitos
df[["idade", "renda", "divida"]].describe()

# Limpeza simples

# Corrigir as categorias
df["estado_civil"] = (df["estado_civil"].str.strip().str.capitalize())

df["estado_civil"].value_counts()

# Tratar a renda ausente

df["renda"] = df["renda"].fillna(df["renda"].mean())

df.head()

# Tratar os valores inválidos
df.loc[df["idade"] > 90, "idade"] = df["idade"].mean().astype(int)
df.loc[df["divida"] < 0, "divida"] = df["divida"].mean()
df.head(20)

# Remover os registros duplicados
print("Duplicados: ", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
df.head(20)

# Criar uma nova informação
df["comprometimento_renda"] = df["divida"] / df["renda"]
df[["renda", "divida", "comprometimento_renda"]].head()
