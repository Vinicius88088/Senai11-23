Dias = int (input ("\n\nDigite a quantidade de dias: "))
Horas = int (input ("Digite a quantidade de horas: "))
Minutos = int (input ("Digite a quantidade de minutos: "))
Segundos = int (input ("Digite a quantidade de Segundos: "))

SegDias = Dias * 86400
SegHoras = Horas * 3600
SegMinutos = Minutos * 60

TotalSeg = SegDias + SegHoras + SegMinutos + Segundos

print ("\nO total dos valores inseridos é de", TotalSeg, "Segundos\n\n")