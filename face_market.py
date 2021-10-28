from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager # linux
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait #####
from selenium.webdriver.support import expected_conditions as CondicaoEsperada ####
import os
import unittest
import re
import time
import socket
import random
import schedule
from datetime import datetime

class Face_market:
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
            poll_frequency=4
                            )
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        #s.connect(('13.224.29.122', 80))
        #dados = s.recv(1024)
        #print(dados)
        #msg = s.recv(1024).decode('UTF-8')
        #print(msg)
    pass

    def Iniciar(self):
        self.logar('login aqui','senha aqui','https://www.facebook.com/marketplace/?ref=app_tab')
    pass

    def logar(self, login_email, login_senha,url):
        self.login_email=login_email
        self.login_senha=login_senha
        self.url=url
        self.driver.get('https://www.facebook.com/')
        self.driver.implicitly_wait(30)
        email=self.driver.find_element_by_xpath('//input[@aria-label="Email ou telefone"]')
        email.send_keys(login_email)
        time.sleep(5)
        senha=self.driver.find_element_by_xpath('//input[@type="password"]')
        senha.send_keys(login_senha)
        time.sleep(5)
        inicio_button=self.driver.find_element_by_xpath('//button[@name="login"]')
        inicio_button.click()
        self.driver.implicitly_wait(30)  
        print('LOGADO')
        time.sleep(120)
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.begin_chat()# o horario de inicio é o schedule e o horario de termino é declarado em logar
    pass

    def begin_chat(self):# inicia o envio
        while True:
            list_picture = self.wait.until(CondicaoEsperada.presence_of_all_elements_located((By.XPATH,'//div[@class="rq0escxv j83agx80 buofh1pr datstx6m ggysqto6 exrn9cbp ojkyduve abpf7j7b l9j0dhe7 k4urcfbm"]')))
            self.driver.implicitly_wait(30)
            for lista_do_for in list_picture:
                time.sleep(3)
                lista_do_for.click()
                self.driver.implicitly_wait(30)
                #primeiro elemento da lista é identificado na janela que abre
                self.conversar()
                try:
                    button_close= self.driver.find_element_by_xpath('//div[@aria-label="Fechar" ]')
                    print('fechado button 1')
                except:
                    try:
                        button_close= self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/span/div/i')
                        print('fechado button 2')
                    except:
                        print('Não foi possivel fechar janela')
                time.sleep(3)
                button_close.click()
                time.sleep(12)
            pass
        pass
    pass

    def conversar(self):
        dir_absolutle = os.path.dirname(os.path.realpath(__file__))
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        self.driver.implicitly_wait(30)
        contacts = self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"]')))
        self.driver.implicitly_wait(30)
        with open(dir_absolutle +'\\bloqueados_face.txt','r+', encoding='UTF-8') as bloqueado:
            cont_or_no_cont =''
            for bloquear in bloqueado:# primeiro IF lê a lista toda, O SEGUNDO decide oq fazer!
                if str(bloquear.strip()) == contacts.text:
                    cont_or_no_cont='CONTEM NA LISTA DE BLOQUEADOS'
                    print('CONTEM NA LISTA DE BLOQUEADOS')
                    break                        
                else:
                    pass 
            pass 
            try:
                if cont_or_no_cont !='CONTEM NA LISTA DE BLOQUEADOS':
                    print('Salvando contato na lista de bloqueados!')
                    bloqueado.write(f'{contacts.text}\n')#screvendo no arquivo bloqueados.txt
                    print('Profissional adicionado a lista de bloqueados!')
                    try:
                        self.escrever_chat(contacts.text)
                    except:
                        print('Não foi possível enviar mensagem ao profissional adicionado agora!')
                        pass
                else:
                    pass 
            except:
                pass     
        bloqueado.close()
    pass
    
    def escrever_chat(self, contacts_name):
        self.contact=contacts_name
        #{str(contacts).split()[0]}
        #str("Eu como abacaxi").split()[0] para pegar a primeira palavra de uma string
        hora_saudacao ='12:00'
        horario_atual = datetime.now()
        hora = int(hora_saudacao.split(':')[0])
        if horario_atual.hour >= hora:
            saudacao='Boa tarde '  
        else:
            saudacao='Bom dia '  
        pass       
        msg_one=(f' {saudacao}{self.contact.split()[0]} !')
        try:
            area_de_texto =self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/label/textarea')))
        except:
            print('area de texto nao localizada')
            pass
        self.driver.implicitly_wait(30)
        try:
            area_de_texto.click()
            time.sleep(2)
            area_de_texto.send_keys(Keys.BACKSPACE)
        except:
            print('Area de texto não detectada! Impossível digitar mensagem!')
            quit()
            pass
        #travar o envio de mensagem para ver se a foto está funcionando
        time.sleep(2)
        self.digite_como_uma_pessoa(msg_one, area_de_texto)
        time.sleep(3)
        button_send= self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[3]/div/span/div/span/div/div/div[1]/div/span/span")
        button_send.click()
        time.sleep(3)        
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
face = Face_market()
face.Iniciar()