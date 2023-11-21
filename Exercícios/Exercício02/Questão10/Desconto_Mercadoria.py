PrecoIniProduto = float (input ("\n\nDigite o preço do produto: "))
PorcentDesconto = float (input ("Digite o valor do percentual de desconto no produto: "))

PorcentCalc = PorcentDesconto / 100

PrecoReajust = PrecoIniProduto * PorcentCalc
PrecoFinalProduto = PrecoIniProduto - PrecoReajust

print ("\n\nVocê economizou: R$", PrecoReajust, "\n")
print ("Total à pagar: R$", PrecoFinalProduto, "\n\n")





