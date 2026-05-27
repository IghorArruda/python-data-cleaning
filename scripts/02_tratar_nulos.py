"""
Script 2: Tratamento de valores nulos
Autor: Ighor Arruda
Objetivo: Preencher ou remover valores faltantes
"""

import pandas as pd

# Carregar os dados
df = pd.read_csv('dados/supermercado_bruto.csv')

print("=" * 50)
print("TRATAMENTO DE VALORES NULOS")
print("=" * 50)

# Contar nulos antes
nulos_antes = df.isnull().sum().sum()
print(f"\n🔍 Nulos ANTES: {nulos_antes}")

# Estratégia de tratamento para cada coluna
# 1. Quantity: preencher com a mediana
mediana_quantity = df['Quantity'].median()
df['Quantity'] = df['Quantity'].fillna(mediana_quantity)

# 2. Tax: preencher com 0 (imposto não aplicado)
df['Tax'] = df['Tax'].fillna(0)

# 3. Payment: preencher com 'Not specified'
df['Payment'] = df['Payment'].fillna('Not specified')

# 4. CustomerType: preencher com 'Unknown'
df['CustomerType'] = df['CustomerType'].fillna('Unknown')

# 5. Gender: preencher com 'Not informed'
df['Gender'] = df['Gender'].fillna('Not informed')

# 6. Rating: preencher com a média
media_rating = df['Rating'].mean()
df['Rating'] = df['Rating'].fillna(media_rating)

# Contar nulos depois
nulos_depois = df.isnull().sum().sum()
print(f"\n✅ Nulos DEPOIS: {nulos_depois}")
print(f"📉 Redução: {nulos_antes - nulos_depois} nulos tratados")

# Salvar dados com nulos tratados
df.to_csv('dados/supermercado_sem_nulos.csv', index=False)
print("\n💾 Arquivo salvo: 'dados/supermercado_sem_nulos.csv'")
