def adicionar_tarefa(lista):
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas(lista):
    if not lista:
        print("A lista de tarefas está vazia.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(lista):
            print(f"{i}. {tarefa}")

def remover_tarefa(lista):
    if not lista:
        print("A lista de tarefas está vazia. Nada para remover.")
        return
    try:
        indice = int(input("Digite o índice da tarefa que deseja remover: "))
        if 0 <= indice < len(lista):
            removida = lista.pop(indice)
            print(f"Tarefa '{removida}' removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def menu():
    tarefas = []
    while True:
        print("\nMenu de Gerenciamento de Tarefas:")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
