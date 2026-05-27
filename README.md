# 🐍 Python Data Cleaning – Projeto de Limpeza de Dados

[![GitHub](https://img.shields.io/badge/GitHub-IghorArruda-blue)](https://github.com/IghorArruda)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ighor-blue)](https://linkedin.com/in/ighor-arruda)

## 👋 Sobre mim
Olá! Sou Ighor Arruda, profissional em transição para Análise de Dados.  
Este projeto demonstra minhas habilidades em **Python com Pandas** para limpeza e transformação de dados.

## 📊 Sobre o Projeto

Este projeto utiliza um **dataset público de vendas de supermercado** (fonte: Kaggle). Os dados originais continham diversos problemas comuns em bases reais:

### Problemas identificados e tratados:

| Problema | Exemplo no dataset |
|----------|-------------------|
| Valores nulos | `Quantity` vazio, `Payment` vazio |
| Duplicatas | Linhas 1 e 3 completamente idênticas |
| Texto inconsistente | `Male`, `male`, `MALE` misturados |
| Maiúsculas/minúsculas | `FEMALE` vs `Female` |

## 📂 Estrutura do Repositório


## 🔧 Etapas da Limpeza

| Script | O que faz | Saída |
|--------|-----------|-------|
| `01_carregar_analisar.py` | Carrega dados e identifica problemas | Relatório no terminal |
| `02_tratar_nulos.py` | Preenche valores vazios (média, mediana, texto padrão) | `supermercado_sem_nulos.csv` |
| `03_remover_duplicatas.py` | Remove linhas repetidas | `supermercado_sem_duplicatas.csv` |
| `04_padronizar_texto.py` | Corrige maiúsculas/minúsculas e inconsistências | `supermercado_limpo.csv` |

## 📈 Resultados

| Métrica | Antes | Depois |
|---------|-------|--------|
| Valores nulos | 5+ | 0 |
| Linhas duplicadas | 2 | 0 |
| Texto padronizado | ❌ | ✅ |

## 🛠️ Tecnologias Utilizadas
- Python 3
- Pandas
- Git & GitHub

## 📊 Fonte dos Dados

Dataset: **Supermarket Sales** (Kaggle)  
🔗 [https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

*Os dados foram modificados para incluir problemas propositais para fins de aprendizado.*

## 🚀 Como Executar

1. Clone o repositório
2. Instale o pandas: `pip install pandas`
3. Execute os scripts em ordem numérica:
   ```bash
   python scripts/01_carregar_analisar.py
   python scripts/02_tratar_nulos.py
   python scripts/03_remover_duplicatas.py
   python scripts/04_padronizar_texto.py

   
📫 Contato
LinkedIn: linkedin.com/in/ighor-arruda

GitHub: github.com/IghorArruda

📌 Este portfólio está em constante evolução.
