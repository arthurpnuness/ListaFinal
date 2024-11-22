
def avaliar_afirmativas(idade, sexo):
    if idade >= 18 and sexo == "feminino":
        return True
    return False

print(avaliar_afirmativas(20, "feminino"))  # Exemplo de avaliação
