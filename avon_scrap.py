from typing import Container
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
#import socket

class Avon_scrap:
    def __init__(self):# declaracao
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox') #linux
        #chrome_options.add_argument('--headless')#linux
        #chrome_options.add_argument('window-size=1920,1480')#linux
        #chrome_options.add_argument('--disable-dev-shm-usage')#linux
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Daniel pc\Desktop\tudo\ESTUDOS_PROGRAMACAO\multi\chromedriver.exe', options=chrome_options)
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chrome_options.add_argument('--log-level=3')
        #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.wait = WebDriverWait( #aqui a variavel self.wait está recebendo o webdriverwait com as caracteristicas
            driver=self.driver,
            timeout= 10,
            poll_frequency=4
                            )
    pass

    def Iniciar(self): # inicia o programa, foi chamado na init---
        print('PROGRAMA PREPARADO')
        self.driver.get('https://www.avon.com.br/encontre-uma-revendedora?sc=1')
        self.driver.implicitly_wait(60)
        iframe=self.driver.find_element_by_xpath('/html/body/main/div[4]/iframe')
        time.sleep(3)
        self.driver.switch_to.frame(iframe)
        time.sleep(3)
        inp_cep=self.driver.find_element_by_xpath('//input[@id="input-3"]')
        time.sleep(3)
        inp_cep.click()
        time.sleep(3)
        inp_cep.send_keys('36081500')
        time.sleep(3)
        inp_cep.send_keys(Keys.ENTER)
        time.sleep(40)
        #iframe.click()
        #iframe.send_keys(Keys.DOWN)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        tentativas=0
        try:
            while tentativas<250:
                try:
                    btn_carregar= self.driver.find_element_by_xpath('//button[@style="color: rgb(252, 187, 255); caret-color: rgb(252, 187, 255);"]')
                    time.sleep(3)
                    btn_carregar.click()
                except:
                    btn_carregar= self.driver.find_element_by_xpath('//button[@style="color: rgb(252, 187, 255); caret-color: rgb(252, 187, 255);"]')
                    time.sleep(3)
                    btn_carregar.click()
                time.sleep(27)
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
                tentativas+=1
            pass
        except:
            pass
        try:
            names_client = self.driver.find_elements_by_xpath('//div[@class="card__title"]')
            self.driver.implicitly_wait(40)
            email_client = self.driver.find_elements_by_xpath('//div[@class="card__email"]')
            self.driver.implicitly_wait(40)
            bairro = self.driver.find_elements_by_xpath('//div[@class="card__address"]')
            self.driver.implicitly_wait(40)
            distancia = self.driver.find_elements_by_xpath('//div[@class="card__distance"]')
            self.driver.implicitly_wait(40)
            tels = self.driver.find_elements_by_xpath('//div[@class="card__phone"]')
            self.driver.implicitly_wait(40)
            text='' 
            for name, email, phone, bar, dist in zip(names_client, email_client,tels,bairro,distancia):
                text+= f'{name.text} | {email.text} | {phone.text} | {bar.text} | {dist.text}\n'
            pass
            print(text)
        except:       
            print('ERRO: TALVEZ RECAPTCHA NÃO ESTAVA FUNCIONANDO')
    pass       
avon = Avon_scrap()
avon.Iniciar() 