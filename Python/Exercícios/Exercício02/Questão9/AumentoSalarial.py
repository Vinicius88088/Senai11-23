SalarioInicial = float (input ("\n\nDigite o salário atual: "))
PorcentAumento = float (input ("Digite o percentual de aumento salarial: "))

PorcentCalc = PorcentAumento / 100

SalarioReajust = SalarioInicial * PorcentCalc
SalarioFinal = SalarioInicial + SalarioReajust

print ("\nO valor do reajuste foi de", SalarioReajust, "R$ com um novo salário de", SalarioFinal, "R$\n\n")





