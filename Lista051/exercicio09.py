''' 9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2
'''

soma_pares = 0
valor = 0

while valor <= 500:
    soma_pares += valor
    valor += 2

print("A soma dos valores pares de 0 até 500 é:", soma_pares)
