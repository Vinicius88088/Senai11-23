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
    if not fila.empty()
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
            file.write(tarefa = "\n")
