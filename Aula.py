''' Arquivo de códigos do curso de Python
    Link do vídeo:
    https://www.youtube.com/watch?v=TW0T3o5ds-k&t=505s
    24/05/2020
'''

import time
print("Alô mundo")
# Aula 01 de python do canal Dev Aprender# Variável
velocidade_da_internet = 50
# Existe tipos de variáveis como Inteiro, Boleanos float e Strings
velocidade_da_internet = 50  # Inteiro
nota_do_aluno = 8.50  # Float
esta_aberto = True  # Boleanos
nome_do_curso = "Jones"  # String

# Identação ou espaçamentos


def PensarPor10Segundos():
    print("pensando")
    time.sleep(10)
    print('Lembrei')


PensarPor10Segundos()

if 10 > 5:
    print('10 é maior que 5')
    if 'hello' == 'hello':
        print("hello")

# 15:42

# Strings

# pode ser usado aspas simples ou duplas
nome_do_instrumentos = "Guitarra Elétrica"
print(nome_do_instrumentos)
# Caracteres de escape
# Quando quer usar aspas na string, barras invertidas
nome_do_filme = "O filme foi \"demais\""
nome_do_filme1 = "O filme foi \n demais"  # Quebra de linha
print(nome_do_filme)
print(nome_do_filme1)

# Formatar strings
aluno = "Jones"
nome_do_curso = "Python"

# Usando variáveis destro da frase usando o f e o nome dentro de chaves. pode colocar expressôes também
mensagem = f"Bem vindo {aluno} ao curso de {nome_do_curso} e o resultado é {5+9}"
print(mensagem)

# 26:20

# Manipulação de strings
nome_do_evento = "Curso de Python"
print(nome_do_evento)
print(nome_do_evento.upper())  # Tudo maiúsculas
print(nome_do_evento.lower())  # Tudo minúscula
print(nome_do_evento.rstrip())  # Remove espaços da direita
print(nome_do_evento.strip())  # Remove espaços e branco iniciais e finais
print(nome_do_evento.lstrip())  # Remove espaços da esquerda
print(nome_do_evento.find("so"))  # Retorna a posição do "so"
print(nome_do_evento.replace("Python", "C++"))  # Subistitui palavras

# Substitui plavras com texto direto
print("https://www.olx.com.br/brasil?q=casas".replace("casas", "apartamentos"))

# 31:08
