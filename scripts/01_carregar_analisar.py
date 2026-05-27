"""
Script 1: Carregar dados e fazer análise inicial
Autor: Ighor Arruda
Objetivo: Identificar problemas nos dados brutos
"""

import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/supermercado_bruto.csv')

print("=" * 50)
print("ANÁLISE INICIAL DOS DADOS")
print("=" * 50)

# 1. Verificar dimensões
print(f"\n📊 Dimensões: {df.shape[0]} linhas e {df.shape[1]} colunas")

# 2. Verificar primeiras linhas
print("\n📋 PRIMEIRAS 5 LINHAS:")
print(df.head())

# 3. Verificar tipos de dados
print("\n📋 TIPOS DE DADOS:")
print(df.dtypes)

# 4. Verificar valores nulos
print("\n🔍 VALORES NULOS POR COLUNA:")
nulos = df.isnull().sum()
print(nulos[nulos > 0] if any(nulos > 0) else "Nenhum valor nulo encontrado!")

# 5. Verificar duplicatas
duplicatas = df.duplicated().sum()
print(f"\n🔄 LINHAS DUPLICADAS: {duplicatas}")

# 6. Estatísticas básicas
print("\n📈 ESTATÍSTICAS BÁSICAS (colunas numéricas):")
print(df.describe())
