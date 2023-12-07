def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha or pilha [-1] != '(':
                return False
            pilha.pop()

    return len(pilha) == 0

#exemplo de funções validação balanceamento
expressao1 = "(2 + 3) * (4 - 1)"
expressao2 = "((5 + 6) * (7 - 2)"
expressao3 = "())("
expressao4 = "((2 + 3)) * (4 - 1)"

print (verifica_parenteses(expressao1))
print (verifica_parenteses (expressao2))
print (verifica_parenteses (expressao3))
print (verifica_parenteses (expressao4))
print (verifica_parenteses (expressao2))

