# Calcular a média de cada aluno;
# Exibir os alunos aprovados e reprovados (média >= 6 para aprovação);
# Permitir salvar um novo arquivo Excel com uma coluna adicional chamada “Situação” (Aprovado/Reprovado).
# O usuário deve escolher o nome do arquivo de saída no console.


import pandas as pd

tabela = pd.read_excel('TrabalhoAluno.xlsx')
print(tabela)
tabela['MÉDIA'] = (tabela['NOTA1'] + tabela['NOTA2']) / 2

tabela.loc[tabela['MÉDIA'] >= 6, 'SITUAÇÃO']= 'APROVADO'
tabela.loc[tabela['MÉDIA'] < 6, 'SITUAÇÃO']= 'REPROVADO'

print(tabela)

tabela.to_excel('TrabalhoAluno_Corrigido.xlsx', index=False) 