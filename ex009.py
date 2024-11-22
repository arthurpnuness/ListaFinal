

def calcular_elegibilidade(renda, pontuacao_credito, despesas):
    renda_liquida = renda - despesas
    elegivel = renda_liquida > 2000 and pontuacao_credito >= 700
    return f"Elegível? {elegivel}, Renda líquida: {renda_liquida}"

# Teste
print(calcular_elegibilidade(5000, 750, 2000))
print(calcular_elegibilidade(3000, 600, 1500))
