#Aumentar em 15% o salário do funcionário
salarioAtual = float(input('Informe o salário atual do funcionário: '))
aumento = salarioAtual * 15 / 100
salarioReajustado = salarioAtual + aumento

print ('O salário de R${:.2f} do funcionário, ao aumentar em 15%, no valor de R${:.2f}, irá passar para R${:.2f}'.format(salarioAtual, aumento, salarioReajustado))