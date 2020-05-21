#!/usr/bin/env python
# coding: utf-8

print ("Olá mundo") # Imprime na tela e pode ser usados áspas simples ou duplas
print ('Didática tech')

print (5+6)

print (10-5)

print (5*3)

print (17/3)

print (2**3)


print (5//2)


print (5%2)

# variáveis 

a = 5


a == 5


c = a + 9

c


print (c)

# também podemos somar duas variáveis


print (a+c)


# In[46]:


# função type para vê qual tipo é a variável


var = 3.5
var1 = 4


type (var),(var1)


var3 = "Teste com python"


var3
type (var3)

var3


# função input, função para inserir dados

nome = input("Qual seu nome? ")


nome


# In[55]:


nome1 = int(input("qual sua idade?"))


type (nome1)


# Formatação

fruta = ("Laranja")

print ("Suco de",fruta) # modo 01

print ("Suco de %s" %fruta) # s de string - d de inteiro (%d) - f de float (%f) - modo 02

print ("Suco de {}".format(fruta))

cor1 = "azul"
cor2 = "verde"

print ("O céu é {0} e meu carro é {1}".format(cor1,cor2))

conta = 17/3
print (conta)

print("A conta deu {:.2f}".format(conta)) # formatar o resultado para dois casas depois da virgula {:.2f}

# Curso para iniciantes - Aula 08 - Condições IF ELSE com Python

comida = "arroz"

if comida == "arroz":
    print("Possui muitas calorias")
else:
    print ("Não sei o que é ")


if comida == "macarrão":
    print("Possui muitas calorias")
elif comida =="pão":  # Mais condições com o elif
    print ("Possui poucas calorias")
elif comida =="arroz":
    print ("Muito bom")
else:
    print ("Não sei o que é ")

if comida != "arroz": # != significa diferente
    print("Possui muitas calorias")
else:
    print ("Não sei o que é ")

# Como usar o looop em python


for i in range(9):
    print (i)

for i in range(9):
    print ("Estou aprendendo python")

for i in range(9):
    print (i*2)

a = 0
for i in range(9):
    a = a + 1
    print (a)

a = 0
for i in range(9):
    a = a + 1
print (a)   # posição influi no resultadoa = 0


palavra = "Matemática"
for i in palavra:
    print (i)

palavra = "Matemática"
for x in palavra:  # pode ser qualquer nome de variável
    print (x)

lista = [2, 23, 43, 21, 56, 34]
for num in lista:
    print (num)


lista = ["Jones", "Lucas", "Flávio", 21, 56, 34]
for num in lista:
    print (num)


# Comandos While e Break em Python

contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
print("Agora deu!!!")

import time
contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
    time.sleep(1)
print("Agora deu!!!")

import time
contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
    if contador == 6:
        break
    time.sleep(1)
print("Agora deu!!!")

numero = int(input("Digite um número "))
fatorial = numero
contador = 1
while (numero-contador)>1:
    fatorial = fatorial*(numero-contador)
    contador +=1
    print (fatorial)
print("{0}! = {1}".format(numero,fatorial))

# Módulos e bibliotecas

import math
math.factorial(5)

import datetime
datetime.date.today(). day # datetime é a bibliotemca, o date é módulo e o today é função - day é um atributo

import datetime  # Posso importar somente o módulo date - from datetime import date
datetime.date.isoformat(datetime.date.today())

from datetime import date
date.isoformat(date.today())


# Criar funções em python


def parabens():
    print(" Parabéns\n Muitos anos de vida")

parabens()


def temletrau(): # Função que não precisa de passar funções
    frase = input("Digite uma frase: ")
    if "u" in frase:
        print("Você usou a letra u ")
    else:
        print("Não tem letra u ")
    


temletrau()


def somaQuadrados(a,b): # Função que precisa de passar parâmetros
    somaQ = a**2 + b**2
    return somaQ

somaQuadrados(2,5) # Mando o valor 2 e 5 para a função para retornar a soma
