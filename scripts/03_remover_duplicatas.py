"""
Script 3: Remoção de duplicatas
Autor: Ighor Arruda
Objetivo: Identificar e remover linhas repetidas
"""

import pandas as pd

# Carregar dados (já com nulos tratados)
df = pd.read_csv('dados/supermercado_sem_nulos.csv')

print("=" * 50)
print("REMOÇÃO DE DUPLICATAS")
print("=" * 50)

# Contar linhas antes
linhas_antes = len(df)
print(f"\n📊 Linhas ANTES: {linhas_antes}")

# Identificar duplicatas
duplicatas = df.duplicated()
total_duplicatas = duplicatas.sum()
print(f"🔄 Duplicatas encontradas: {total_duplicatas}")

# Mostrar duplicatas (se houver)
if total_duplicatas > 0:
    print("\n🔍 Exemplo de linhas duplicadas:")
    print(df[duplicatas].head(3))

# Remover duplicatas (manter primeira ocorrência)
df = df.drop_duplicates()

# Contar linhas depois
linhas_depois = len(df)
print(f"\n📊 Linhas DEPOIS: {linhas_depois}")
print(f"🗑️ Removidas: {linhas_antes - linhas_depois} linhas")

# Salvar dados sem duplicatas
df.to_csv('dados/supermercado_sem_duplicatas.csv', index=False)
print("\n💾 Arquivo salvo: 'dados/supermercado_sem_duplicatas.csv'")
