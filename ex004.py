

def verificar_idade_sexo(idade, sexo):
    if idade < 18:
        categoria = "menor de idade"
    elif idade <= 59:
        categoria = "adulto"
    else:
        categoria = "idoso"
    return f"Pessoa do sexo {sexo} é {categoria}."

# Teste
print(verificar_idade_sexo(17, 'masculino'))
print(verificar_idade_sexo(25, 'feminino'))
print(verificar_idade_sexo(65, 'masculino'))
