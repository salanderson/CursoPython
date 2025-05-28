import pandas as pd 

# importar a base de dados

tabela_vendas = pd.read_excel('vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja

# quantidade de produtos vendidos por loja

# ticket medio por produto em cada loja

# enviar um e-mail com o relatorio

