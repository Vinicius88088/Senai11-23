class Fila: 
    
    #Definição de uma fila sem tamanho e sem elementos
    def __init__(self):
        self.itens = []
    
    #Tamanho da fila
    def tamanho(self):
        return len(self.itens)
    
    #Definindo função 'enfileirar'
    def enfileirar (self, elemento):
        self.itens.append(elemento)

    #valida se a lista está vazia
    def esta_vazia(self):
        return len(self.itens) == 0
    
    #Função desenfilerar
    def desenfilerar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0) #remoção da fila
    
fila = Fila()

fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")
fila.enfileirar("D")

tamanho = fila.tamanho()
print("\n\n\nTamanho da fila: ", tamanho)

valor = fila.desenfilerar()
print ("Item removido: ", valor)

tamanho = fila.tamanho()
print("Tamanho da fila: ", tamanho)

valor = fila.desenfilerar()
print ("Item removido: ", valor)

