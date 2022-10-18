salarioAtual = float(input('Informe o salário atual do funcionário: '))
aumento = float(input('Informe, em porcentagem, quanto será o aumento: '))
valorAumento = salarioAtual * aumento / 100
salarioReajustado = salarioAtual + aumento

print ('O salário de R${:.2f} do funcionário, ao aumentar em {:.2f}%, no valor de R${:.2f}, irá passar para R${:.2f}'.format(salarioAtual, aumento, valorAumento, salarioReajustado))