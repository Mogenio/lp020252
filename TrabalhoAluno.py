# Calcular a média de cada aluno;
# Exibir os alunos aprovados e reprovados (média >= 6 para aprovação);
# Permitir salvar um novo arquivo Excel com uma coluna adicional chamada “Situação” (Aprovado/Reprovado).
# O usuário deve escolher o nome do arquivo de saída no console.


import pandas as pd

caminho_arquivo = r'C:\Users\gabri\OneDrive\Documentos\NotaAluno\TrabalhoAluno.xlsx'

try:
    tabela = pd.read_excel(caminho_arquivo, engine='openpyxl')

    print("--- Tabela Original ---")
    print(tabela)

    tabela['MÉDIA'] = (tabela['NOTA1'] + tabela['NOTA2']) / 2

    tabela.loc[tabela['MÉDIA'] >= 6, 'SITUAÇÃO'] = 'APROVADO'
    tabela.loc[tabela['MÉDIA'] < 6, 'SITUAÇÃO'] = 'REPROVADO'

    print("\n--- Tabela Calculada ---")
    print(tabela)

    
    nome_usuario = input("\nDigite o nome para salvar o arquivo (sem extensão): ")
    
    
    caminho_saida = caminho_arquivo.replace('TrabalhoAluno.xlsx', 'TrabalhoAluno_Corrigido.xlsx')
    
    tabela.to_excel(caminho_saida, index=False)
    print(f"\nSucesso! Arquivo salvo em: {caminho_saida}")

except FileNotFoundError:
    print("ERRO: O Python não encontrou o arquivo. Verifique se o caminho na linha 6 está correto.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")