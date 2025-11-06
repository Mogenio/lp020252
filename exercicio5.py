import random
#05- Faça um programa que leia um número inteiro e mostre 
#na tela o seu sucessor e o seu antecessor.

def q5(): 

    numero = int(input('Digite um número: '))

    print('O número é: {}' .format(numero))

    sucessor = numero + 1
    antecessor = numero - 1

    print('O sucessor do número é: {} '.format(sucessor))
    print('O antecessor do número é: {} '.format(antecessor))

#06- crie um algoritmo que leia um número e mostre o seu dobro
#triplo e raiz quadrada
def q6():

    numero = int(input('Digite um número: '))
    dobro = numero * 2
    triplo = numero * 3
    raiz = dobro ** 0.5
    raiz2 = triplo ** 0.5

    print('O número digitado foi {}, e o dobro dele é {} e a raiz quadrada dele é {} '.format(numero, dobro, raiz))
    print('O número digitado foi {}, e o triplo dele é {} e a sua raiz quadrada é {} '.format(numero, triplo, raiz2))

#07- Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média.
def q7():

    nome = input('Digite seu nome: ')
    n1 = int(input('Digite a primeira nota: '))
    n2 = int(input('Digite a segunda nota: '))
    media = (n1 + n2)/2

    print('A média do aluno {} foi {} '.format(nome, media))


#08- Escreva um programa que leia um valor em metros e o exiba
#convertido em centimentros e milimetros.
def q8():

    metros = float(input('Digite um valor em metros: '))
    centimetros = metros * 100
    milimetros = metros * 1000

    print('O valor do metros é {}, e o centimetros dele é {} e o seu milimetros é {} '.format(metros, centimetros, milimetros))

#09- Faça um programa que leia um número qualquer e mostre
#na tela a sua tabuada 
def q9():

    numero = int(input('Digite um número a ser multiplicado: '))
    n1 = numero * 1
    n2 = numero * 2
    n3 = numero * 3
    n4 = numero * 4
    n5 = numero * 5
    n6 = numero * 6
    n7 = numero * 7
    n8 = numero * 8
    n9 = numero * 9
    n10 = numero * 10

    print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

#10- crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar.
def q10():

    carteira = float(input('Digite o valor que você tem:$'))
    dolar = carteira / 5.34

    print('Tenha na carteira ${:.2f}, e vou poder comprar em US${:.2f} em dolar' .format(carteira, dolar))


#11- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a 
#quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta 
#pinta um area de 2m quadrado
def q11():
    larg = float(input('Largura da parede: '))
    alt = float(input('Altura da parede: '))
    área = larg * alt
    print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
    tinta = área / 2
    print('Para pintar essa parede, você precisará de {}l de tinta.' .format(tinta))

# 12- Faça um algoritmo que leia o preoço de um produto e mostre seu novo preço
# com 5% de desconto
def q12():

    preço = float(input('Qual é o preço do produto? R$'))
    novo = preço - (preço * 5 / 100)
    print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.' .format(preço, novo))

# 13- Escreva um programa que converta uma temperatura digitando em graus
#  Celsius e converta pata graus Fahrenheit
def q13():
    c = float(input('Informe a temperatura em °C: '))
    f = 9 * c / 5 + 32
    print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')