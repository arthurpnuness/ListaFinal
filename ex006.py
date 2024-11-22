
def validar_expressao(a, b, c):
    print(f"A || (B && C): {a or (b and c)}")
    print(f"!A && B && C: {not a and b and c}")
    print(f"!(A && B && !C): {not (a and b and not c)}")

validar_expressao(True, False, True)

