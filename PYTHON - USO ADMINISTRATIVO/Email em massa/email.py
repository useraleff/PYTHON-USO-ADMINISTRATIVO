from email.mime import message
import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# importamos todas as bibliotecas necessárias

MY_ADDRESS = 'email@user' # definimos aqui a informação referente ao email utilizado para o envio
PASSWORD = 'user_password' # definimos aqui a senha do email utilizado

def get_contacts(mycontacts):
    # coletamos os dados do arquivo mycontacts.txt
    
    names = []
    emails = []
    with open(mycontacts, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
    # criamos uma lista com os nomes e emails presentes no arquivo

def read_template(message):
    # lemos o arquivo message.txt
    
    with open(message, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
    # abrimos o arquivo, retornando como Template

def main():
    names, emails = get_contacts('mycontacts.txt')
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.domain', port='')
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    # configuramos o servidor SMTP

    for name, email in zip(names, emails): # para cada contato, envie o email:
        msg = MIMEMultipart()       

        message = message_template.substitute(PERSON_NAME=name.title())
        # adiciona o nome da pessoa real para o modelo de mensagem

        print(message)
        # imprime o corpo do email

        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="TEST MAIL" # Assunto do email
        # configura os parâmetros da mensagem
        
        msg.attach(MIMEText(message, 'plain'))
        # adiciona a mensagem ao corpo

        filename = 'file.pdf'
        
        attachment = open('file.pdf','rb')
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # caso queira incluir um anexo, basta importar ele para a pasta do código e alterar o file.pdf para o nome e extensão do arquivo
        
        msg.attach(part)
        attachment.close()
        
        s.send_message(msg)
        del msg
        # envia a mensagem através do servidor
        
    s.quit()
    # termina o servidor SMTP e fecha a conexão

    
if __name__ == '__main__':
    main()