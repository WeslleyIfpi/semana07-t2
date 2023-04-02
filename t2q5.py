def ordena(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        if n2 < n3 :
            return n1, n2, n3
        else:
            return n1, n3, n2
    
    elif n2 < n1 and n2 < n3:
        if n1 < n3:
            return n2, n1, n3
        else:
            return n2, n3, n1
        
    elif n3 < n1 and n3 < n2:
        if n1 <n2:
            return n3, n1, n2
        else:
            return n3, n2, n1

def main():
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    numero3 = float(input('Digite o terceito número: '))

    saida1, saida2, saida3 = ordena(numero1, numero2, numero3)

    print(f'Do menor para o maior: ')
    print(f'{saida1}')
    print(f'{saida2}')
    print(f'{saida3}')

if __name__ == '__main__':
    main()

