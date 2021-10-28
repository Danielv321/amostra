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

class G_scrap:
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
            poll_frequency=3
                            )
    pass

    def Iniciar(self): # inicia o programa, foi chamado na init---
        print('PROGRAMA PREPARADO')
        # colocar a url da pesquisa
        self.driver.get('https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALeKk00nYE9xjvc84YUG4ZfsJ6Tkrkzfzg:1629117550603&q=igreja+juiz+de+fora&rflfq=1&num=10&sa=X&ved=2ahUKEwi0l5rnx7XyAhWRpZUCHfIDAzwQjGp6BAgHEFo&biw=1366&bih=625#rlfi=hd:;si:2751612696434572705,l,ChNpZ3JlamEganVpeiBkZSBmb3JhSIH-3o7jq4CACFofEAAYABgBGAIYAyITaWdyZWphIGp1aXogZGUgZm9yYZIBBmNodXJjaJoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1VOTmRHVk1NRlpSRUFFqgEOEAEqCiIGaWdyZWphKAw;mv:[[-21.7076356,-43.337896199999996],[-21.7778653,-43.4473801]]')
        time.sleep(60) 
        cond_loop = True
        while cond_loop == True:
            self.coletar_dados()
            try:
                button_next=self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'//span[text()="Próximo"]')))
                button_next.click()
                time.sleep(30)
            except:
                try:
                    button_next=self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'//span[text()="Mais"]')))
                    button_next.click()
                    time.sleep(30)
                except:
                    print('Fim...................')
                    cond_loop = False
        pass
    pass

    def coletar_dados(self):
        companys=self.driver.find_elements_by_xpath('//div[@class="dbg0pd"]')
        self.driver.implicitly_wait(30)
        for element in companys:
            element.click()
            time.sleep(10)
            try:
                address_company = self.driver.find_element_by_xpath('//span[@class="LrzXr"]')
                address_company_tx=address_company.text
            except:
                address_company_tx='Não mencionado'
                pass
            try:
                phone_company=self.wait.until(CondicaoEsperada.presence_of_element_located((By.XPATH,'//span[@class="LrzXr zdqRlf kno-fv"]')))
                print(f'{element.text} | {address_company_tx} | {phone_company.text} ')
            except:
                phone_company='Não mencionado'
                print(f'{element.text} | {address_company_tx} | {phone_company}')
            time.sleep(5)
        pass
    pass
scrap=G_scrap()
scrap.Iniciar()