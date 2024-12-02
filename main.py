from db import init_db, create_task, get_tasks, update_task_status, delete_task

def menu():
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar status de uma tarefa")
    print("4. Deletar uma tarefa")
    print("5. Sair")

def main():
    init_db()
    while True:
        menu()
        choice = input("Escolha uma opção: ")
        if choice == "1":
            title = input("Título: ")
            description = input("Descrição: ")
            status = input("Status (Pendente, Em andamento, Concluído): ")
            create_task(title, description, status)
        elif choice == "2":
            tasks = get_tasks()
            for task in tasks:
                print(task)
        elif choice == "3":
            task_id = int(input("ID da tarefa: "))
            status = input("Novo status: ")
            update_task_status(task_id, status)
        elif choice == "4":
            task_id = int(input("ID da tarefa: "))
            delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
