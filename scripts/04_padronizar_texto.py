"""
Script 4: Padronização de textos
Autor: Ighor Arruda
Objetivo: Corrigir maiúsculas/minúsculas, espaços e inconsistências
"""

import pandas as pd

# Carregar dados
df = pd.read_csv('dados/supermercado_sem_duplicatas.csv')

print("=" * 50)
print("PADRONIZAÇÃO DE TEXTOS")
print("=" * 50)

# Lista de colunas de texto
colunas_texto = ['Branch', 'City', 'CustomerType', 'Gender', 'ProductLine', 'Payment']

print("\n🔧 Aplicando padronização...")

for coluna in colunas_texto:
    # Remover espaços extras e converter para título (primeira letra maiúscula)
    df[coluna] = df[coluna].astype(str).str.strip().str.title()
    
    # Correção específica para Gender (padronizar Male/Female)
    df['Gender'] = df['Gender'].replace({
        'Male': 'Male',
        'MALE': 'Male',
        'male': 'Male',
        'Female': 'Female',
        'FEMALE': 'Female',
        'female': 'Female',
        'Not Informed': 'Not specified'
    })

print("✅ Textos padronizados!")

# Verificar resultado
print("\n📋 VALORES ÚNICOS APÓS PADRONIZAÇÃO:")
print(f"Gender: {df['Gender'].unique()}")
print(f"CustomerType: {df['CustomerType'].unique()}")
print(f"Payment: {df['Payment'].unique()}")

# Salvar dados FINAIS limpos
df.to_csv('dados/supermercado_limpo.csv', index=False)
print("\n💾 ARQUIVO FINAL SALVO: 'dados/supermercado_limpo.csv'")

# Resumo final
print("\n" + "=" * 50)
print("RESUMO DA LIMPEZA")
print("=" * 50)
print(f"✅ Nulos tratados")
print(f"✅ Duplicatas removidas")
print(f"✅ Textos padronizados")
print(f"📊 Dados finais: {len(df)} linhas")
