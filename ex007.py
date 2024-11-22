


def tabela_verdade_chuva_sol_avaliacao(chuva, sol, avaliacao):
    print(f"Chuva: {chuva}, Sol: {sol}, Avaliação G1: {avaliacao}")
    print(f"Teremos G1 caso chova ou faça sol: {chuva or sol}")

tabela_verdade_chuva_sol_avaliacao(True, False, True)
