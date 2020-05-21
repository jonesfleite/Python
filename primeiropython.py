#!/usr/bin/env python
# coding: utf-8

# In[29]:


print ("Olá mundo") # Imprime na tela e pode ser usados áspas simples ou duplas


# In[30]:


print ('Didática tech')


# In[31]:


print (5+6)


# In[32]:


print (10-5)


# In[33]:


print (5*3)


# In[34]:


print (17/3)


# In[35]:


print (2**3)


# In[36]:


print (5//2)


# In[37]:


print (5%2)


# In[38]:


# variáveis 


# In[39]:


a = 5


# In[40]:


a == 5


# In[41]:


c = a + 9


# In[42]:


c


# In[43]:


print (c)


# In[44]:


# também podemos somar duas variáveis


# In[45]:


print (a+c)


# In[46]:


# função type para vê qual tipo é a variável


# In[47]:


var = 3.5
var1 = 4


# In[48]:


type (var),(var1)


# In[49]:


var3 = "Teste com python"


# In[50]:


var3
type (var3)


# In[51]:


var3


# In[52]:


# função input, função para inserir dados


# In[53]:


nome = input("Qual seu nome? ")


# In[54]:


nome


# In[55]:


nome1 = int(input("qual sua idade?"))


# In[56]:


type (nome1)


# In[57]:


# Formatação


# In[58]:


fruta = ("Laranja")


# In[59]:


print ("Suco de",fruta) # modo 01


# In[60]:


print ("Suco de %s" %fruta) # s de string - d de inteiro (%d) - f de float (%f) - modo 02


# In[61]:


print ("Suco de {}".format(fruta))


# In[62]:


cor1 = "azul"
cor2 = "verde"


# In[63]:


print ("O céu é {0} e meu carro é {1}".format(cor1,cor2))


# In[64]:


conta = 17/3
print (conta)


# In[65]:


print("A conta deu {:.2f}".format(conta)) # formatar o resultado para dois casas depois da virgula {:.2f}


# In[66]:


# Curso para iniciantes - Aula 08 - Condições IF ELSE com Python


# In[67]:


comida = "arroz"


# In[68]:


if comida == "arroz":
    print("Possui muitas calorias")
else:
    print ("Não sei o que é ")


# In[69]:


if comida == "macarrão":
    print("Possui muitas calorias")
elif comida =="pão":  # Mais condições com o elif
    print ("Possui poucas calorias")
elif comida =="arroz":
    print ("Muito bom")
else:
    print ("Não sei o que é ")


# In[71]:


if comida != "arroz": # != significa diferente
    print("Possui muitas calorias")
else:
    print ("Não sei o que é ")


# In[72]:


# Como usar o looop em python


# In[1]:


for i in range(9):
    print (i)


# In[2]:


for i in range(9):
    print ("Estou aprendendo python")


# In[3]:


for i in range(9):
    print (i*2)


# In[5]:


a = 0
for i in range(9):
    a = a + 1
    print (a)


# In[7]:


a = 0
for i in range(9):
    a = a + 1
print (a)   # posição influi no resultadoa = 0


# In[8]:


palavra = "Matemática"
for i in palavra:
    print (i)


# In[9]:


palavra = "Matemática"
for x in palavra:  # pode ser qualquer nome de variável
    print (x)


# In[12]:


lista = [2, 23, 43, 21, 56, 34]
for num in lista:
    print (num)


# In[13]:


lista = ["Jones", "Lucas", "Flávio", 21, 56, 34]
for num in lista:
    print (num)


# In[14]:


# Comandos While e Break em Python


# In[23]:


contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
print("Agora deu!!!")


# In[26]:


import time
contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
    time.sleep(1)
print("Agora deu!!!")


# In[28]:


import time
contador = 0 
while contador < 10:
    contador = contador + 1
    print(contador, "Ainda é menor que 10")
    if contador == 6:
        break
    time.sleep(1)
print("Agora deu!!!")


# In[2]:


numero = int(input("Digite um número "))
fatorial = numero
contador = 1
while (numero-contador)>1:
    fatorial = fatorial*(numero-contador)
    contador +=1
    print (fatorial)
print("{0}! = {1}".format(numero,fatorial))


# In[3]:


# Módulos e bibliotecas


# In[7]:


import math
math.factorial(5)


# In[16]:


import datetime
datetime.date.today(). day # datetime é a bibliotemca, o date é módulo e o today é função - day é um atributo


# In[19]:


import datetime  # Posso importar somente o módulo date - from datetime import date
datetime.date.isoformat(datetime.date.today())


# In[21]:


from datetime import date
date.isoformat(date.today())


# In[1]:


# Criar funções em python


# In[10]:


def parabens():
    print(" Parabéns\n Muitos anos de vida")


# In[11]:


parabens()


# In[13]:


def temletrau(): # Função que não precisa de passar funções
    frase = input("Digite uma frase: ")
    if "u" in frase:
        print("Você usou a letra u ")
    else:
        print("Não tem letra u ")
    


# In[16]:


temletrau()


# In[17]:


def somaQuadrados(a,b): # Função que precisa de passar parâmetros
    somaQ = a**2 + b**2
    return somaQ


# In[19]:


somaQuadrados(2,5) # Mando o valor 2 e 5 para a função para retornar a soma


# In[ ]:




