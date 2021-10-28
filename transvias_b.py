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

class Trans_vias:
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
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Daniel pc\Desktop\multi\chromedriver.exe', options=chrome_options)
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chrome_options.add_argument('--log-level=3')
        #self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        #self.wait = WebDriverWait( #aqui a variavel self.wait está recebendo o webdriverwait com as caracteristicas
        #    driver=self.driver,
        #    timeout= 10,
        #    poll_frequency=4
        #                    )
    pass

    def Iniciar(self): # inicia o programa, foi chamado na init---
        print('PROGRAMA PREPARADO')
        self.driver.get('https://www.transvias.com.br/transportadoras/estados/rio-de-janeiro')
        self.driver.implicitly_wait(120) 
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        names_company = self.driver.find_elements_by_xpath('//h2[@class="m-boxCompany__A__info__name__txt ng-binding"]')
        roll=0
        while roll <= len(names_company):
            try:
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
                self.driver.implicitly_wait(60)
            except:
                pass
            names_company=self.driver.find_elements_by_xpath('//h2[@class="m-boxCompany__A__info__name__txt ng-binding"]')
            self.driver.implicitly_wait(40)
            roll+=1
        pass

        #while roll <= 2000:
        #    self.driver.execute_script('window.scrollBy(0,75)')
        #    self.driver.implicitly_wait(40)
        #    roll+=1
        #pass
        
        #names_company = self.driver.find_elements_by_xpath('//h2[@class="m-boxCompany__A__info__name__txt ng-binding"]')
        self.driver.implicitly_wait(40)
        tels=self.driver.find_elements_by_xpath('//span[@class="ng-binding"]')
        self.driver.implicitly_wait(40)
        text=''
        for name, phone in zip(names_company,tels):
            text+= f'{name.text} | {phone.text}\n'
        pass
        print(text)
        
trans = Trans_vias()
trans.Iniciar()