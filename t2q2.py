def ehPar(numero):
    return numero % 2 == 0

def main():
    numero = int(input('Digite um numero entr 100 e 999: '))
    pares = 0
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 100) % 10

    if numero > 99 and numero < 1000:
        if ehPar(centena):
            pares += 1
        if ehPar(dezena):
            pares += 1
        if ehPar(unidade):
            pares += 1

    print(f'No numero digitado há o total de {pares} número pares.')

if __name__ == '__main__':
    main()