import webbrowser
# importamos a biblioteca webbrowser
# é preciso ter o aplicativo do whatsapp instalado para que o código funcione adequadamente

while True:
    # Para manter o código em looping
    wpp = "http://wa.me/55"
    # definindo a variável wpp com o link de início do WhatsApp

    numero = str(input("Informe o número de telefone com DDD: "))
    # define a variavel numero como str e pede para que o user informe o número de telefone que deseja abrir um chat
    # precisa ser str porque vamos adicionar o número de telefone ao link wpp

    link = wpp + numero
    # criamos então uma nova variável, unindo o wpp com o numero informado pelo user

    webbrowser.open(link)
    # rodamos o código, ele abrirá o navegador padrão e em seguida o aplicativo do WhatsApp no computador do usuário
