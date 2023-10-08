#inprimir sem que o usuario insira os números
A = []
num = 1
#len vê quantos caracteres está insirido na variavel
while len(A) < 10:
#append adiciona um elemeno ao final da lista, modificando a lista original e aumentando seu tamanho
    A.append(num)
# coloca o número impar para o próximo número impar, pulando os pares
    num += 2
#printa a lista A
print(A)


#inprimir os números com o usuario ensirindo os mesmos
A = []
#len vê quantos caracteres está insirido na variavel
while len(A) < 10:
    #input para o usuario digitar os números
    num = int(input("Digite um número: "))
    #retorna verdadeiro/True quando o número é ímpar e Falso/False quando o número é par.
    if num % 2 != 0:
        A.append(num)
print(A)