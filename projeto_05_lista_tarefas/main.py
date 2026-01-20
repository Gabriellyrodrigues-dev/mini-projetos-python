tarefas = []

def mostrar_menu():
    print("\n=== Projeto 05 — Lista de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")

def adicionar():
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append({"texto": tarefa, "concluida": False})
        print("✅ Tarefa adicionada!")
    else:
        print("❌ Tarefa vazia.")

def listar():
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return
    print("\n--- Tarefas ---")
    for i, t in enumerate(tarefas, start=1):
        status = "✅" if t["concluida"] else "⏳"
        print(f"{i}. {status} {t['texto']}")

def concluir():
    listar()
    if not tarefas:
        return
    try:
        n = int(input("Número da tarefa para concluir: "))
        tarefas[n-1]["concluida"] = True
        print("✅ Tarefa concluída!")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

def remover():
    listar()
    if not tarefas:
        return
    try:
        n = int(input("Número da tarefa para remover: "))
        removida = tarefas.pop(n-1)
        print(f"🗑️ Removida: {removida['texto']}")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        concluir()
    elif opcao == "4":
        remover()
    elif opcao == "0":
        print("Até mais!")
        break
    else:
        print("❌ Opção inválida.")
