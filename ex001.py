'''Métodos de Lógica Dedutiva e Indutiva

Explique a diferença entre o método dedutivo e o método indutivo. Em seguida, escreva um código que utilize lógica dedutiva para verificar se um número é par ou ímpar, e um código com lógica indutiva que faz uma lista dos números ímpares de 1 até 100.'''

'''- Lógica dedutiva parte de uma regra geral para determinar um caso específico.
- A regra geral aqui é:
    - Um número é **par** se for divisível por 2 (n%2==0).
        
        n%2==0n \% 2 == 0
        
    - Caso contrário, é **ímpar** (n%2=0).
        
        n%2≠0n \% 2 \neq 0'''

def entrada():
## Função para receber o numero
    numero = int(input('Digite um numero: '))
    return numero

def processamento(numero):
## Função para ver se o numero é par ou impar
    if numero % 2 == 0:
        print('O numero é par')
    else:
        print('O numero é impar')

def saida():
## Função de execução
    numero = entrada()
    processando = processamento(numero)

saida()

'''- Lógica indutiva observa padrões para gerar generalizações.
- O padrão aqui é:
    - Números ímpares de 1 a 100 são aqueles em que n%2=0.
        
        n%2≠0n \% 2 \neq 0'''

def verificacao():

##  Laço com o for para percorrer de 1 a 101 
    for i in range(1, 101):
        if i % 2 != 0: ## Condição para aparecer apenas o numeros impares
            print(i)
        
def main():
    
    verificando = verificacao() 

main()