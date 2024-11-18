def menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Ver todas as tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas(tarefas):
    if tarefas:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

def remover_tarefa(tarefas):
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida: "))
            if 1 <= indice <= len(tarefas):
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")
    else:
        print("Não há tarefas para remover.")

def main():
    tarefas = []
    
    while True:
        menu()
        opcao = input("Escolha a opção (1-4): ")
        
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            remover_tarefa(tarefas)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal para rodar o programa
main()
