while True:

    baseCalculo = float(input('Digite o valor total do produto (Para decimais, se deve usar ponto e não vírgula): '))
    aliquota = float(input('Informe o valor do IPI: '))
    valorIpi = baseCalculo * (aliquota/100)
    somaIpi = baseCalculo + valorIpi
    print ('''O valor do IPI é de {}.
O total da nota será de {}'''.format(valorIpi, somaIpi))
