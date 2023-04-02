def eh_impar(numero):
    return not numero % 2 == 0

def conta_impares(quatidade):
    saida = 'Nenhum dígito é ímpar.'
    if quatidade == 1:
        saida = 'Apenas um dígito é ímpar.'
    elif quatidade == 2:
        saida = 'Os dois dígitos são ímpares.'
    
    return saida
        
def main():
    entrada = int(input('Digite um número entra 10 e 99: '))
    impares = 0
    dezena = entrada // 10
    unidade = entrada % 10

    if eh_impar(dezena):
        impares += 1
    if eh_impar(unidade):
        impares += 1
    
    print(f'Em {entrada}: {conta_impares(impares)}')

if __name__ == '__main__':
    main()
    