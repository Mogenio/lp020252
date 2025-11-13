import random
# import math
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, raiz))

# 01- Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção inteira 
def q1():
    
    num = float(input('Digite um número qualquer: '))
    print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
    
# 02- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo 
# retangulo, calcule e mostre o comprimento da hipotenusa
def q2():
    import math
    co = float(input('Comprimento do cateto oposto: '))
    ca = float(input('Comprimento do cateto adacente: '))
    hi = math.hypot(co, ca)
    print('A hipotenusa vai medir {:.2f}'.format(hi))
    

    # 03- Faça um programa que leia um angulo qualquer e mostre na tela o valor da seno, cosseno
    # e tangente desse angulo 

    def q3():
        import math 
        an = float(input('Digite o ângulo que você deseja: '))
        seno = math.sin(math.radians(an))
        print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
        print('A hipotenusa vai medir {:.2f}'.format(hi))
        cosseno = math.cos(math.radians(an))
        print('O ângulo de {} tem o  COSSENO de{:.2f}'.format(an, cosseno))
        tangente = math.tan(math.radians(an))

# 04- Um professor quer sortea um dos seus quatros alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome escolhido 
def q4():
    from random import choice
    n1 = str(input('Primeiro aluno: '))
    n2 = str(input('Segundo aluno: '))
    n3 = str(input('Terceiro aluno: '))
    n4 = str(input('Quarto aluno: '))
    lista = [n1, n2, n3, n4]
    escolhido = choice(lista)
    print('O aluno escolhido foi {}'.format(escolhido))


# 05- O mesmo do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
def q5():
    from random import shuffle
    n1 = str(input('Primeiro aluno: '))
    n2 = str(input('Segundo aluno: '))
    n3 = str(input('Terceiro aluno: '))
    n4 = str(input('Quarto aluno: '))
    lista = [n1, n2, n3, n4]
    shuffle(lista)
    print('A ordem de apresentação será ')
    print(lista)



# 06- Faça um programa em Python que abra e reproduza o audio de um arquivo MP3


questao = int(input('Questao a ser executada: '))
eval(f'q{questao}()')
