import pandas as pd

tabela = pd.read_excel('TrabalhoAlunos.xlsx')
print(tabela)
tabela.loc[tabela['MÉDIA'] >= 6, 'SITUAÇÃO']= 'APROVADO'
tabela.loc[tabela['MÉDIA'] > 6, 'SITUAÇÃO']= 'REPROVADO'


print(tabela)