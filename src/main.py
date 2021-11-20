from services.CYK import CYK

def main():
    cyk = CYK()

    print('--' * 14)
    print("            CYK")
    print('--' * 14)
    print('[ 1 ] Testar palavra')
    print('[ 2 ] Sair')
    print('--' * 14)
    option = int(input("Escolha uma opção: "))
    while option != 2:
        if option == 1:
            string = input("Insira a palavra: ")
            print('--' * 14)
            cyk.testString(string)
        print('--' * 14)
        option = int(input("Escolha uma opção: "))

if __name__ == '__main__':
    main()