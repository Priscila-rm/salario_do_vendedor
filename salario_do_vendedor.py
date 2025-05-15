nome_do_vendedor = input("qual é seu nome?: ")
salario = float(input("qual é o seu salario?"))
valor_vendido = float(input ("qual valor foi vendido?"))

comissão = valor_vendido * 0.15
valor_total= comissão + salario
print(valor_total)


