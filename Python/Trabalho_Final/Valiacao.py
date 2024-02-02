import queue

def adicionar_tarefa(tarefa, fila):
    fila.put(tarefa)
    salvar_tarefas(fila, "tarefas.txt")

def tarefa_concluida(pilha, fila):
    if not fila.empty():
        tarefa_concluida = fila.get()
        pilha.append(tarefa_concluida)
        salvar_tarefas(fila, "tarefas.txt")
        salvar_tarefas_concluidas(pilha, "tarefas_concluidas.txt")
    else:
        print("Não há tarefas pendentes.")

def proxima_tarefa(fila):
    if not fila.empty():
        proxima = fila.queue[0]
        print("Próxima tarfa a ser feita: ", proxima)
    else:
        print("Não há tarefas pendentes.")

def exibir_tarefas_pendentes(fila):
    if not fila.empty():
        print("Tarefas pendentes: ")
        for tarefa in list (fila.queue):
            print("-", tarefa)
    
    else:
        print("Não há tarefas pensdentes")

def exibir_tarefas_concluidas(pilha):
    if pilha:
        print("Tarefas Concluídas: ")
        for index, tarefa in enumerate(pilha[::-1], start=1):
            print(f"{index}. {tarefa}")
        else:
            print("Não há tarefas concluídas.")

def salvar_tarefas(fila, arquivo):
    with open(arquivo, "w") as file:
        for tarefa in reversed(pilha):
            file.write(tarefa + "\n")

def salvar_tarefas_concluidas(pilha, arquivo):
    with open(arquivo, "w") as file:
        for tarefa in reversed(pilha):
            file.write(tarefa + "\n")

def carregar_tarefas(fila, arquivo):
    try:
        with open(arquivo, "r") as file:
            for linha in file:
                file.put(linha.strip())
    except FileNotFoundError:
        pass

def carregar_tarefas_concluidas(pilha, arquivo):
    try:
        with open(arquivo, "r") as file:
            for linha in file:
                pilha.append(linha.strip())
    except FileNotFoundError:
        pass

fila_tarefas = queue.Queue()
pilha_tarefas_concluidas = []

carregar_tarefas(fila_tarefas, "tarefas.txt")
carregar_tarefas_concluidas(pilha_tarefas_concluidas, "tarefas_concluidas.txt")

adicionar_tarefa("Ler livro", fila_tarefas)
adicionar_tarefa("Fazer Exercícios de lógica", fila_tarefas)
tarefa_concluida(pilha_tarefas_concluidas, fila_tarefas)
proxima_tarefa(fila_tarefas)
exibir_tarefas_pendentes(fila_tarefas)
exibir_tarefas_concluidas(pilha_tarefas_concluidas)