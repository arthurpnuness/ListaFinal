

def verificar_operadores_relacionais(a, b):
    resultados = {
        "a < b": a < b,
        "a > b": a > b,
        "a <= b": a <= b,
        "a >= b": a >= b,
        "a == b": a == b,
        "a != b": a != b
    }
    return resultados

def verificar_operadores_logicos(x, y):
    resultados = {
        "x and y": x and y,
        "x or y": x or y,
        "not x": not x
    }
    return resultados

# Teste para operadores relacionais
a = 5
b = 10
print("Operadores Relacionais:")
relacionais = verificar_operadores_relacionais(a, b)
for operacao, resultado in relacionais.items():
    print(f"{operacao}: {resultado}")

# Teste para operadores lógicos
x = True
y = False
print("\nOperadores Lógicos:")
logicos = verificar_operadores_logicos(x, y)
for operacao, resultado in logicos.items():
    print(f"{operacao}: {resultado}")
