tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    else:
        print("Tarefa não encontrada.")

def listar_tarefas():
    if not tarefas:
        print("Sua lista de tarefas está vazia.")
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nova_tarefa = input("Digite a nova tarefa: ")
        adicionar_tarefa(nova_tarefa)
    elif opcao == '2':
        tarefa_remover = input("Digite a tarefa a ser removida: ")
        remover_tarefa(tarefa_remover)
    elif opcao == '3':
        listar_tarefas()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")