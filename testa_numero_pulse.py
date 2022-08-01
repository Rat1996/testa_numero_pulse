from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

#=====================================Funçoes

#Aguarda tela carregar

def aguardarCarregamento(driver: webdriver):
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

#inicia o navegador

def iniciarNavegador(url: str = "http://189.3.77.72:8080/SipPulseAdmin/pages/login/login.jsf"):
    # Iniciar Chrome
    driver = webdriver.Chrome("chromedriver")

    # Ler página  de login
    driver.get(url)
    return driver

#Faz o login na pulse

def fazerLogin(username: str, password: str, driver: webdriver):
    # Encontrar elemento 'username' e inserir texto
    driver.find_element(By.NAME, "j_username").send_keys(username)

    # Encontrar elemento 'password' e inserir texto
    driver.find_element(By.NAME, "j_password").send_keys(password)

    # Clicar em login utilizando o classe como referência
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td/div/input").click()

    # Aguardar login terminar de submeter
    aguardarCarregamento(driver)

    return True

#Clica no menu Subscriber/assinante

def clickSubscriber(el:str, by:str, driver: webdriver):
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td/form/center/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/a").click()
    aguardarCarregamento(driver)
    return True

#Pesquisa o assinante

def pesquisarSubscriber(subs: str, by:str, driver: webdriver):
    driver.find_element(By.NAME, "frmSubscriberFilter:filterData").send_keys(subs)
    driver.find_element(By.ID, "frmSubscriberFilter:j_id130").click()
    aguardarCarregamento(driver)
    return True


def clicaBtEditar(el:str, by:str, driver: webdriver):
    driver.find_element(By.XPATH, '//*[@id="frmSubscriberFilter:subscribersList:0:j_id152"]/a/img').click() #"//*td[contains(text(),'(3130030000)')]/parent::tr/td[2]::a").click()
    aguardarCarregamento(driver)
    return True

def encontrarElemento(el:str, by:str, driver: webdriver):
    return driver.find_element(by, el)

def clickEmUmElemento(el:str, by:str, driver: webdriver):
    driver.find_element(by, el).click()


def editarCallerID(callerid:str, driver: webdriver):
    driver.find_element(By.ID, "frmSubscriber:rpid").clear()
    driver.find_element(By.ID, "frmSubscriber:rpid").send_keys(callerid)
    aguardarCarregamento(driver)
    return True

def salvarPagina(driver: webdriver):
    driver.find_element(By.ID, "frmSubscriber:j_id1078").click()
    time.sleep(3)
    driver.find_element(By.ID, "frmSubscriber:j_id1072").click()
    aguardarCarregamento(driver)
    return True



#def ProgramaCompleto():
#    arquivo_numeros = open('numeros_pra_teste.txt', 'r')
#    resposta = input('Iniciar navegador? y/n')
#        if resposta == 'y':
#            driver = iniciarNavegador()
#            fazerLogin('carlos.sena', 'edbb515c', driver)
#            clickSubscriber('Subscriber', 'Subscriber', driver)
#            pesquisarSubscriber('3130030000', 'Search', driver)
#            time.sleep(2)
#            clicaBtEditar('Editar','Editar', driver)
#        else:
#        break;
#
#    resposta2 = input('Iniciar teste? y/n')
#    count = 0
#        if resposta2 == 'y':
#            print('Começando a testar')
#            for line in arquivo_numeros:
#                editarCallerID(line, driver)
#                salvarPagina(driver)
#                print('testar agora')
#                time. sleep(9)
#                count += 1
#            pass
#        pass


def banner():
    banner = """
 _____         _                      
|_   _|       | |                     
  | | ___  ___| |_ __ _               
  | |/ _ \/ __| __/ _` |              
  | |  __/\__ \ || (_| |              
 _\_/\___||___/\__\__,_|              
| \ | |                               
|  \| |_   _ _ __ ___   ___ _ __ ___  
| . ` | | | | '_ ` _ \ / _ \ '__/ _ \ 
| |\  | |_| | | | | | |  __/ | | (_) |
\_| \_/\__,_|_| |_| |_|\___|_|  \___/ 
                        1.0 por Carlos              

    """
    print(banner)


#=====================================Execução

banner()
driver = iniciarNavegador()
fazerLogin('usuario_pulse', 'senha_pulse', driver)
clickSubscriber('Subscriber', 'Subscriber', driver)
pesquisarSubscriber('login_subscriber', 'Search', driver)
time.sleep(2)
clicaBtEditar('Editar','Editar', driver)


#====================Altera os numeros e salva pagina=============================

# opening the file in read mode
my_file = open("numeros.txt", "r")
# reading the file
data = my_file.read()  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print("Números para testar:")
print(data_into_list)
my_file.close()

#data_into_list =
for x in data_into_list:
    editarCallerID(x, driver)
    salvarPagina(driver)
    print('testando ' + x)
    time.sleep(9)

#=================================================
#clickEmUmElemento()
aguardarCarregamento(driver)
#lerTabelaUsuariosCDR(driver)
# encerrarConexaoDrive(driver)
exit()


#funcional sem funcao de ler arquivo e linha
