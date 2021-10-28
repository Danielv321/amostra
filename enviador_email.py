import os
import smtplib
from email.message import EmailMessage
import time

#configurar login
endereco_email ='daniel@previsegmg.com.br'
senha='Daniel102030'

#criando email

msg=EmailMessage()
msg['subject'] = 'Copia teste (a/c:Daniel)'
msg['From']=endereco_email
msg['To']=  'danielrpmg@gmail.com'#aqui eu coloco funcao
msg.set_content('Olá, esse é o texto do email...')

#Fazer envio
with smtplib.SMTP_SSL('mail.previsegmg.com.br',465) as smtp:
    smtp.login(endereco_email,senha)
    smtp.send_message(msg)
    time.sleep(180)
    print('mensagem enviada')
pass