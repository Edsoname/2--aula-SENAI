'''
print("Bom dia!") # teste para rodar VS |CODE
'''

# entrada de dados/ armanzenando um dado

'''
nome = 'Senai'
print(f"olá {nome}")
'''
# 2 variáveis 

# entrada de dados de 2 notas de uma médiia de notas!

'''
nota1 = float(input("Digite uma nota 0 a 10:\n"))
nota2 = float(input("DIgite uma nota de 0 a 10:\n"))
média = (nota1 + nota2)/2
#print(f"sua média é {média:.2f}")
print('a média',(nota1 +nota2)/2)

'''

# operadores do python

# Aritiméticos: +,/,%,**,//
# Relacionais: ==, != , > ,< ,>= ,<= 
# lógicos: and ,or ,not 


# true or false
'''
a = 10; b = 22
print(a < b and b > a)

'''

# Faça um programa  que calcule a divisão inteira e a 
# exponenciação entre dois números fornecidos pelo usuario.

'''
num1 = int(input("Digite o 1º número:\n"))
num2 = int(input("DIgite o 2º número:\n"))

print("DIvisão inteira:",num1 // num2)
print("exponenciação:",num1 ** num2)

'''

# Estrurturas de decisão (if, else, Elif)
# pessa uma idade e diga se apessoa pode votar


'''
idade = int(input("Digite sua idade:\n"))
if idade >= 16:
    print('Pode votar!')
else:
    print('Não pode votar!')
'''

# escreva um programa que receba duas idades 
# e infiorme quem é mais velho ou tem a mesma idade

'''
idade1 = int(input("Digite a 1º idade:\n"))
idade2 = int(input("Digite a 2º idade:\n"))

if idade1 > idade2:
    print(f"A 1º pessoa é mais velha")
elif idade1 < idade2:
    print(f"A 2º Pessoa é mais velha")
else:
    print("As duas Pessoas tem a mesma idade")

'''

# Faça um programa que defina qual tipo de Bolo 
# foi escolhido pelo usuario e apresente o sabor escolhido.

'''

tipo_bolo = input("Escolha um tipo de bolo ! Chocolate,Morango,Baunilha,Cenoura\n")
if tipo_bolo == "Chocolate":
    print("Você escolheu Bolo de chocolate!")
elif tipo_bolo == "Cenoura":
    print("Voçê escolheu Bolo de Cenoura!")
elif tipo_bolo == "Morango":
    print("Voce escolheu Bolo de Morango")
elif tipo_bolo == "Baunilha":
    print("Você escolheu Bolo de Baunilha!")
else:
    print("Você escolheu Bolo fora da lista!")

'''

# Faça um programa que indique que dia da semana 
# estará disponivel para consulta! 
'''
Dias = int(input("Digite um número de 1 a 7:\n"))
if Dias == 1:
    print("Segunda-Feira disponivel")
elif Dias ==2:
    print("Terça-feira disponivel")
elif Dias == 3:
    print("Quarta-Feira disponivel")
elif Dias == 4:
    print("Quinta-feira disponivel")
elif Dias == 5:
    print("Sexta-feira disponivel")
elif Dias == 6:
    print("Sábado disponivel")
elif Dias == 7:
    print("Domingo disponivel")
else:
    print("não à dia disponivel")

'''


'''
# != diferente de

a = 5
b = 7
if a != b:
    print("os valores são diferentes")
else:
    print(" os valores são iguais")

'''


# Faça um programa que verifique se uma pessoa pode dirigir

'''
idade =18
tem_carteira = False
tem_carteira = True
idade = int(input("Digite sua idade:\n"))
if idade >= 18 and tem_carteira: # verdade
    print('pode dirigir')
else:
    print("não pode dirigir")

'''
# Esacreva um programa que verifique se a pessoa tem 
# idade entre 18 e 65 anos e se ela é maior de idade.


'''
idade = int(input("Digite a sua idade:\n"))
if idade >= 18 and idade <= 65:
    print(" você está na faixa etária de trabalho!")
elif idade <18:
    print(" Você é menor de idade!")
else: 
    print("você é maior de idade , mas está fora da faixa etária de trabalho!")
'''

# explicação da classificação:
# criança(0 a 12 anos): faixa etária infantil
# Adolescente(13 a 17 anos): jovens em idade escolar
# Adulto(18 a 30 anos): jovens adultos
# Adultos(31 a 60 anos): adultos experientes
# vida do INSS(61 a mais de 100 anos): idoso ou aposentado

'''
idade = int(input("digite a sua idade:\n"))

if 0 <= idade <= 12:
    print("Você é uma criança!")
elif 13 <= idade <= 17:
    print(" Você é um adolescente!")
elif 18 <= idade <= 30:
    print(" Você é adulto!")
elif 31 <= idade <= 60:
    print(" você é um adulto experiente!")
elif 61 <= idade <= 100:
    print("Você é um idoso aposentado pelo INSS!")
else: 
    print(" Idade inválida ou fora do intervalo esperado!")
'''

'''
# Laços (for e while)
# for repete um bloco por um número conhecido de vezes

for i in range(1,29999999): 
    print(i)
    if 1 == 100:
        break
'''

# while repete enquanto uma condição for verdadeira.

'''
x = 0
while x <120000:
    print(x)
    x += 1 
'''

# imprima os números de 1 a 25 usando um laço FOR
'''
for i in range(1,26):
    print(i)

'''


# listas em python
'''
frutas = ["maçã","Banana","laranja","Uva"]
frutas.remove("Banana") # remove banana da lista
frutas.append("Abacate") # adiciona Abacate na lista
frutas.insert(2,"melancia")# adiciopna frutas na posição 2
frutas.insert(3,"caju") # adiciona Melancia na posição 3
print(frutas[3])
'''

# crie uma lista de nomes e imprima 1 por linha FOR

# 3 nomes
'''
nomes = ['James','Bruno','Henrique']
for nome in nomes:
    print(nomes)

'''

# peça 5 números ao usúario e armazene numa lista e imprima a soma.

'''
numeros = []
for i in range(5):
    n = int(input(f"digite o {i+1}° número\n"))
    numeros.append(n)
print('soma:', sum(numeros))

'''










    