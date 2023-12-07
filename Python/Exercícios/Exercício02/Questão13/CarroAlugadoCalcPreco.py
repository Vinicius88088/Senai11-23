KMPercorrido = float (input ("\n\n\nInsira o valor em KM da distância percorrida com o veículo: "))

TempoDeUso = float (input ("\nInsira a quantidade de dias em que ficou com o veículo: "))

print ("\n\nO valor a pagar será de: ")


ValorCombustivel = 0.15 * KMPercorrido

print ("\nR$", ValorCombustivel,"referente ao valor do combustível do veículo no aluguél")


print ("\nE")


ValorAluguel = 89 * TempoDeUso

print ("\nR$", ValorAluguel,"referente ao valor a ser pago pelo aluguél do veículo.")


ValorTotalPag = ValorCombustivel + ValorAluguel

print ("\nPortando o valor total é de R$", ValorTotalPag, "\n")