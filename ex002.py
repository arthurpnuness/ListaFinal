

def menu():
    print('1- Inteiro (int)')
    print('2- Ponto Flutuante (float)')
    print('3- String (str)')
    print('4- Booleano (bool)')
    print('5- Sair')
    opc = int(input("Selecione a opção que voce deseja saber como funciona: "))
    return opc

def main():
    opc = 0

    while opc != 5:
        opc = menu()
        if opc == 1:
            print('int (inteiro): Armazena números inteiros (ex.: 10, -3).\n Funcionalidade dos Inteiros: Usado para cálculos matemáticos sem partes fracionárias.')
        elif opc == 2:
            print('float (ponto flutuante): Armazena números com decimais (ex.: 3.14, -2.5). \n Funcionalidade do float: Usado para cálculos matemáticos que requerem precisão decimal.')
        elif opc == 3:
            print('str (string): Armazena texto ou sequência de caracteres (ex.: "Python", "123"). \n Funcionalidade das String: Usado para manipular texto, como concatenar ou formatar strings.')
        elif opc == 4:
            print('bool (booleano): Armazena valores de verdade, True ou False. \n Funcionalidade dos booleanos: Usado em condições e tomadas de decisão (ex.: if, while).')
        else:
            print('Saindoo..')
            break

main()

