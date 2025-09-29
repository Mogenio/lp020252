#05- Faça um programa que leia um número inteiro e mostre 
#na tela o seu sucessor e o seu antecessor.

#numero = int(input('Digite um número: '))

#print('O número é: {}' .format(numero))

#sucessor = numero + 1
#antecessor = numero - 1

#print('O sucessor do número é: {} '.format(sucessor))
#print('O antecessor do número é: {} '.format(antecessor))

#06- crie um algoritmo que leia um número e mostre o seu dobro
#triplo e raiz quadrada

#numero = int(input('Digite um número: '))
#dobro = numero * 2
#triplo = numero * 3
#raiz = dobro ** 0.5
#raiz2 = triplo ** 0.5

#print('O número digitado foi {}, e o dobro dele é {} e a raiz quadrada dele é {} '.format(numero, dobro, raiz))
#print('O número digitado foi {}, e o triplo dele é {} e a sua raiz quadrada é {} '.format(numero, triplo, raiz2))

#07- Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média.

#nome = input('Digite seu nome: ')
#n1 = int(input('Digite a primeira nota: '))
#n2 = int(input('Digite a segunda nota: '))
#media = (n1 + n2)/2

#print('A média do aluno {} foi {} '.format(nome, media))


#08- Escreva um programa que leia um valor em metros e o exiba
#convertido em centimentros e milimetros.

#metros = float(input('Digite um valor em metros: '))
#centimetros = metros * 100
#milimetros = metros * 1000

#print('O valor do metros é {}, e o centimetros dele é {} e o seu milimetros é {} '.format(metros, centimetros, milimetros))

#09- Faça um programa que leia um número qualquer e mostre
#na tela a sua tabuada 

#numero = int(input('Digite um número a ser multiplicado: '))
#n1 = numero * 1
#n2 = numero * 2
#n3 = numero * 3
#n4 = numero * 4
#n5 = numero * 5
#n6 = numero * 6
#n7 = numero * 7
#n8 = numero * 8
#n9 = numero * 9
#n10 = numero * 10

#print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

#10- crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar.

#carteira = int(input('Digite o valor que você tem:$'))
#dolar = carteira / 5.34

#print('Tenha na carteira ${}, e vou poder comprar em US${} em dolar' .format(carteira, dolar))


#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a 
#quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta 
#pinta um area de 2m quadrado

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura *altura

litros_tinta = area / 2

print(f'\nA área da parede é de {area:.2f} m\u00b2.')
print(f'Você precisará de {litros_tinta: 2f} litros de tinta para pintá-la.')