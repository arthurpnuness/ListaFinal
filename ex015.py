

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    chute = 0
    while chute != numero_secreto:
        chute = int(input("Adivinhe o número: "))
        if chute < numero_secreto:
            print("Muito baixo!")
        elif chute > numero_secreto:
            print("Muito alto!")
        else:
            print("Parabéns, você acertou!")

# Teste
# jogo_adivinhacao()
