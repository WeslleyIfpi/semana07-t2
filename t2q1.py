def contaLetras(nome):
    return len(nome)

def main():
    nome = input('Seu nome: ').strip()
    estCivil = int(input('Seu estado estCivil (1 - casado, 2 - solteiro): '))

    if estCivil == 1:
        nomeConjuge = input('Nome do conjuge: ').strip()
        print(f'Seu nome + o do seu conjude tem: {contaLetras(nomeConjuge) + contaLetras(nome) } letras')
    else:
        print(f'Seu nome tem: {contaLetras(nome)} letras.')
        

if __name__ == '__main__':
    main()
