from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager # linux
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait #####
from selenium.webdriver.support import expected_conditions as CondicaoEsperada ####
import unittest
import re
import time
import socket
import random
import schedule
from datetime import datetime

class Multi:
    def __init__(self):# declaracao
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox') #linux
        #chrome_options.add_argument('--headless')#linux
        #chrome_options.add_argument('window-size=1920,1480')#linux
        #chrome_options.add_argument('--disable-dev-shm-usage')#linux
        #chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Daniel pc\Desktop\tudo\ESTUDOS_PROGRAMACAO\multi\chromedriver.exe', options=chrome_options)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.wait = WebDriverWait( #aqui a variavel self.wait está recebendo o webdriverwait com as caracteristicas
            driver=self.driver,
            timeout= 10,
            poll_frequency=3
                            )
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        #s.connect(('13.224.29.122', 80))
        #dados = s.recv(1024)
        #print(dados)
        #msg = s.recv(1024).decode('UTF-8')
        #print(msg)
    pass
    
    def Iniciar(self): # inicia o programa, foi chamado na init---
        print('PROGRAMA PREPARADO')
        self.reconectar()
        #def comecar():
        #    #aproveitando a funcao reconectar para conectar com a conta de acordo com o horario
        #    #self.logar('emailaqui','senhaaqui','URL DA SUA PESQUISA AQUI','18:00')
        #    #self.logar('emailaqui','senhaaqui','URL DA SUA PESQUISA AQUI','22:00')
        #    ##coloco outra conta para logar, respeitando o horario fim da outra
        #    time.sleep(5)
        #pass
        ##fuso de  4 hras Falkenstein
        #schedule.every().monday.at('18:45').do(comecar)
        #schedule.every().tuesday.at('14:03').do(comecar)
        #schedule.every().wednesday.at('15:30').do(comecar)
        #schedule.every().thursday.at('16:40').do(comecar)
        #schedule.every().friday.at('14:07').do(comecar)
        #
        #while True:
        #    schedule.run_pending()#roda a tarefa pendente
        #    time.sleep(1)
        #pass    
    pass

    def logar(self, login_email, login_senha,url,horario_fim):
        self.horario_fim=horario_fim
        self.login_email=login_email
        self.login_senha=login_senha
        self.url=url
        self.driver.get('https://conta.olx.com.br/acesso/')
        self.driver.implicitly_wait(30)
        try:
            time.sleep(5)
            cookies = self.driver.find_element_by_xpath('//button[text()="Entendi"]')
            self.driver.implicitly_wait(10)
            cookies.click()
        except:
            pass
        email=self.driver.find_element_by_xpath('//input[@type="email"]')
        email.send_keys(login_email)
        time.sleep(5)
        senha=self.driver.find_element_by_xpath('//input[@type="password"]')
        senha.send_keys(login_senha)
        time.sleep(5)
        inicio_button=self.driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[2]/form/button')
        inicio_button.click()
        self.driver.implicitly_wait(30)  
        print('LOGADO')
        time.sleep(120)
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.begin_chat(horario_fim)# o horario de inicio é o schedule e o horario de termino é declarado em logar
    pass

    def begin_chat(self,horario_termino):# inicia o envio
        try:
            time.sleep(5)
            cookies = self.driver.find_element_by_xpath('//button[text()="Entendi"]')
            self.driver.implicitly_wait(10)
            cookies.click()
            time.sleep(5)
        except:
            pass
        try:
            time.sleep(5)
            cookies_novo_olx= self.driver.find_element_by_xpath('//div[@class="zi8mbi-6 famXXQ"]')
            self.driver.implicitly_wait(10)
            cookies_novo_olx.click()
        except:
            pass
        self.horario_termino=horario_termino
        listado_pagina = self.driver.find_elements_by_xpath('//h2[@class="sc-1mbetcw-0 fKteoJ sc-ifAKCX jyXVpA"]')
        for lista_do_for in listado_pagina:
            time.sleep(3)
            lista_do_for.click()
            self.driver.implicitly_wait(30)
            #primeiro elemento da lista é identificado na janela que abre
            self.driver.implicitly_wait(30)
            window_after = self.driver.window_handles[1] #primeiro elemento da lista é identificado na janela que abre
            self.driver.switch_to.window(window_after)
            self.conversar()
            self.driver.switch_to.window(self.driver.window_handles[0])
            try:
                time.sleep(5)
                cookies_novo_olx= self.driver.find_element_by_xpath('//div[@class="zi8mbi-6 famXXQ"]')
                self.driver.implicitly_wait(10)
                cookies_novo_olx.click()
            except:
                pass
            self.parar_operacao(horario_termino)
        pass
        try:
            self.passar_page()
        except:
            print('erro passar_page')
            pass
        print(self.driver.current_url)
        try:
            self.begin_chat(horario_termino)# begin recebe horario_termino que será usado como horario_parar em parar_operacao
        except:
            print('erro begin')
            pass
    pass
       
    def conversar(self):
        try:              
            prof_or_no_prof=self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//span[text()="PRO"]')))
            self.driver.implicitly_wait(10)
            if prof_or_no_prof.text=='PRO':
               print('ANUNCIO PROFISSIONAL')
               time.sleep(5)
               self.driver.close()
               time.sleep(3)
            else:
                pass
        except:
            self.continua_chat()
            self.driver.close() 
        pass       
    pass

    def deslogar(self):
        print('PREPARANDO PARA DESLOGAR')
        time.sleep(10)
        try:
            menu = self.driver.find_element_by_xpath('//a[@class="sc-hZSUBg sc-esOvli sc-fYiAbW bLxRgJ sc-cMhqgX geppGK"]')
            self.driver.implicitly_wait(30)
            menu.click()
            sair=self.driver.find_element_by_xpath("//a[text()='Sair']")
            self.driver.implicitly_wait(10)
            sair.click()
        except:
            try:
                menu = self.driver.find_element_by_xpath('//a[@class="sc-hZSUBg sc-esOvli sc-fYiAbW bLxRgJ sc-cMhqgX geppGK"]')
                self.driver.implicitly_wait(30)
                menu.click()
                sair=self.driver.find_element_by_xpath("//*[@id='header-container']/div/div[1]/header/div[3]/div[1]/nav/ul/li[11]/a")
                self.driver.implicitly_wait(10)
                sair.click()
            except:           
                print('Não foi possível SAIR da aplicação!')
                quit()
                pass   
        pass
    pass

    def parar_operacao(self,horario_parar):
        self.horario_parar = horario_parar
        horario_atual = datetime.now()
        hora = int(horario_parar.split(':')[0])
        minuto = int(horario_parar.split(':')[1])
        if horario_atual.hour == hora and horario_atual.minute >=minuto:
            try:
                self.deslogar()
                self.driver.implicitly_wait(10)
                print('deslogado!')
                time.sleep(300)# vai dormir por 1h hora ou nao
            except:
                print(' ERRO AO DESLOGAR!!!')
                quit()
                pass
        else:
            pass
    pass

    def reconectar(self):
        meio_expediente ='18:00'
        horario_atual = datetime.now()
        hora = int(meio_expediente.split(':')[0])
        minuto = int(meio_expediente.split(':')[1])
        if horario_atual.hour >= hora and horario_atual.minute >=minuto:
            #segunda opção de conta
            self.logar('emailaqui','senhaaqui','URL DA SUA PESQUISA AQUI','18:00')
            #self.logar('emailaqui','senhaaqui','URL DA SUA PESQUISA AQUI','22:00')
        else:
            #primeira opção de conta
            self.logar('emailaqui','senhaaqui','URL DA SUA PESQUISA AQUI','18:00')
            
            pass
    pass

    def continua_chat(self):
        print('tarefa continuar chat')
        try:
            print(self.driver.current_url)
            butao_chat =self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//span[@color="white"]')))
            butao_chat.click()
            print('ABRINDO CHAT!!!')
        except:
            print('falha ao abrir janela de conversa')
            try:
                print('tentando logar novamente')
                self.reconectar()
                time.sleep(5)
            except:
                pass
        pass                           
        # o bot vai tentar 1 vez fazer contato       
        try:
            time.sleep(5)
            cookies = self.driver.find_element_by_xpath('//button[text()="Entendi"]')
            self.driver.implicitly_wait(10)
            cookies.click()
        except:
            print('cokie nao fechado 1')
            pass
        try:
            time.sleep(5)
            cookies_olx= self.driver.find_element_by_xpath('//div[@class="zi8mbi-6 famXXQ"]')
            self.driver.implicitly_wait(10)
            cookies_olx.click()
        except:
            print('cokie nao fechado 2')
            pass 
        try:
            msg_do_olx =self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,"//span[text()='Ver outras dicas']")))
            if msg_do_olx.text !='':
                print('digitando...')
                self.escrever()
                print('PRIMEIRA TENTATIVA ACERTADA 1')
            else:
                pass
        except:
            print('msg_do_olx não achado')
            pass
    pass
    def escrever(self):
        hora_saudacao ='12:00'
        horario_atual = datetime.now()
        hora = int(hora_saudacao.split(':')[0])
        if horario_atual.hour >= hora:
            saudacao='Boa tarde'  
        else:
            saudacao='Bom dia'  
        pass      
        #escreva a mensagem que desejar dentro da variavel msg_one  
        msg_one = (f'{saudacao}! MENSAGEM AQUI')
        area_de_texto =self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'//textarea[@placeholder="Digite uma mensagem..."]')))
        self.driver.implicitly_wait(30)
        try:
            area_de_texto.click()
        except:
            print('Area de texto não detectada! Impossível digitar mensagem!')
            quit()
            pass
        self.digite_como_uma_pessoa(msg_one, area_de_texto)
        time.sleep(2)
        area_de_texto.send_keys(Keys.ENTER)
        time.sleep(2)
    pass

    def digite_como_uma_pessoa(self, texto, elemento):
        for letter in texto:
            if letter == '\n': # aqui está o código que identifca a quera de linha e usa o shift enter
                elemento.send_keys(Keys.SHIFT, Keys.ENTER)
                time.sleep(random.randint(1,4) / 65)
            else:
                elemento.send_keys(letter)
                time.sleep(random.randint(1,4) / 65)
        pass
    pass

    def passar_page(self):
        passa_page = self.driver.find_element_by_xpath('//*[text()="Próxima pagina"]')
        self.driver.implicitly_wait(30)
        passa_page.click()
    pass
chat=Multi()
chat.Iniciar()
