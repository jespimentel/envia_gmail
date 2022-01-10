#################################################################################
# Automatização de envio de e-mails para a Campanha do CSMP do biênio 2022-2023 #
# José Eduardo de Souza Pimentel                                                #
# 16 Out. 2021                                                                  #
#################################################################################
import os
import sys
import smtplib
from email.message import EmailMessage
from secreto import senha, usuario

print ('\n\nBem vindo, LEGITIMIDADE E COMPROMISSO COM O MP!')
print ('_______________________________________________\n\n')
# Configuração da conta de e-mail emissora
usuario = usuario
senha = senha
servidor = 'smtp.gmail.com'
porta = 587

# Dados específicos da reunião
assunto = input ('Entre com o assunto: ')
data_e_hora = input('Entre com a data e hora da reunião: ')
link = input ('Entre com o link da reunião: ')
lista_destinatarios = input ('Entre com a lista de destinatários (separados somente por espaço): ')
lista_destinatarios = lista_destinatarios.split(' ')

# Inclusão dos conselheiros e assessores na lista
conselheiros = ['xxx@uol.com.br', 'xxx@mpsp.mp.br', 'xxx@uol.com.br', 'xxx@uol.com.br', 'xxx@gmail.com', 'xxx@gmail.com']
auxiliares = ['xxx@gmail.com', 'xxx@uol.com.br']
lista_destinatarios = list(set(lista_destinatarios + auxiliares)) # Exclui valores repetidos

# Corpo de mensagem
corpo_msg = f"""
Prezado(a) colega,

Nós da chapa LEGITIMIDADE E COMPROMISSO COM O MP - integrada por candidatos ao CSMP biênio 2022/2023 
- temos a elevada honra de convidá-lo(a) para a reunião virtual que estamos agendando para o dia {data_e_hora}.

Entre por este link: {link}

Ficaremos honrados com a sua presença!
Até lá e um forte e fraternal abraço.

A. C. P. 
J. C. M. B. 
M. A. F. L. 
N. L. S. A. 
P. J. J. 
S. M.

Conheça o nosso site: https://www.legitimidademp.com

Facebook: https://www.facebook.com/LegitimidadeMP

YouTube: https://www.youtube.com/channel/UC7UsZZSB1YBQjB_Y5S-sOHA

"""

# Confirmação dos dados
confirmacao = input(f'Confirma data e hora do evento(s/n)? {data_e_hora} ')
if confirmacao != 's' and confirmacao != 'S': sys.exit()
confirmacao = input(f'Confirma o link da reunião (s/n)? {link} ')
if confirmacao != 's' and confirmacao != 'S': sys.exit()
print('Serão enviados e-mails para', len(lista_destinatarios), 'destinatários.')
for l in lista_destinatarios:
    print (l, end=' ')
confirmacao = input ('\nConfirma essa informação (s/n)? ')
if confirmacao != 's' and confirmacao != 'S': sys.exit()
print ('Campo assunto do e-mail: ', assunto)
confirmacao = input ('Confirma essa informação (s/n)? ')
if confirmacao != 's' and confirmacao != 'S': sys.exit()
print ('Mensagem:\n', corpo_msg)
confirmacao = input ('Confirma a mensagem acima (s/n)? ')
if confirmacao != 's' and confirmacao != 'S': sys.exit()

# Criação e envio dos e-mails
# Criação
for destinatario in lista_destinatarios:
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = 'Legitimidade e Compromisso com o MP'
    msg['To'] = destinatario
    msg.set_content(corpo_msg)

# Envio
    try:
        with smtplib.SMTP(servidor, porta) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(usuario, senha)
            smtp.send_message(msg)
        print ('E-mail enviado para ', destinatario)
    except:
        print('Não consegui enviar para ', destinatario)

print ('\n\nO programa foi concluído!')
os.system("pause")
