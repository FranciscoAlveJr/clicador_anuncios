from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import getpass
from random import random

params = {
    'latitude': -7.113694623257644,
    'longitude': -34.82716943928752,
    'accuracy': 100
}

usuario = getpass.getuser()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('prefs', {'geolocation': True})
options.add_argument(f"user-data-dir=C:/Users/{usuario}/AppData/Local/Google/Chrome/User Data/")
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)
driver.get('https://www.google.com.br/')

with open('keys.txt', 'r+', encoding='UTF-8') as r:
    keys_w = r.readlines()

pesq = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

for letra in keys_w[-1].replace('\n', ''):
    pesq.send_keys(letra)
    sleep(random())
sleep(random())
pesq.send_keys(Keys.ENTER)

wa = WebDriverWait(driver, 1000)
action = ActionChains(driver)

# wa.until(EC.presence_of_element_located((By.CLASS_NAME, 'd8lRkd')))

page = driver.page_source
soup = bs(page, 'html.parser')


sites = ['liguelojadasbaterias', 'lojadasbateriasjoaopessoa', 'lojadasbateriaspe', 'lojadasbateriasjp', 'vertiv', 'mourafacil', 'ferreiracosta', 'gigapromo', 'izito']

concorrentes = ['sentinelabaterias', 'batcenter', 'drbaterias', 'expressbaterias', 'joiabaterias', 'araujobateriasligue', 'liguetopbateriasmumbaba', 'ligueazbaterias', 'expressbateriasmanaira', 'casadoescapamento', 'germanobaterias', 'liguesobateriaseacessorios', 'evaldobaterias', 'marcelobaterias', 'centraldasbateriaspe', 'expressbateriasmanaira', 'expressbateriasbessa', 'expressbateriascentro', 'expressbaterias', 'expressbateriasjoseamerico', 'expressbateriasmangabeira', 'ng-baterias-centro', 'shoppingdasbateriaspe', 'mercantilbaterias', 'bateriarecife', 'casadabateria', 'trocarapidabaterias', 'heliarexpress', 'liguecasadoescamento', 'ldmbaterias', 'reiforbaterias', 'nilbaterias']
 
print()
print('ANÚNCIOS CLICADOS:')

while True:
    for k in keys_w:
        try:
            sleep(1)
            page = driver.page_source
            soup = bs(page, 'html.parser')
            links = driver.find_elements(By.CLASS_NAME, 'd8lRkd')
            anuncios = soup.find_all('div', {'class':'d8lRkd'})

            for i in range(len(anuncios)):
                try:
                    page = driver.page_source
                    soup = bs(page, 'html.parser')
                    links = driver.find_elements(By.CLASS_NAME, 'd8lRkd')
                    anuncios = soup.find_all('div', {'class':'d8lRkd'})

                    a = anuncios[i].find('span', {'class': 'x2VHCd OSrXXb qzEoUe'}).text
                    # url_anuncio = a[a.find('h'):a.rfind('/')]
                    url2 = a[a.find('.')+1:]
                    url_t = url2[:url2.find('.')]
                    if url_t in concorrentes:
                        print(url_t)
                        links[i].click()
                        sleep(5)
                        driver.back()
                except AttributeError:
                    continue
                except Exception as erro:
                    continue
    
            sleep(random())
            pesq_return = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input')
            pesq_return.clear()
            sleep(0.5)
            for letra in k.replace('\n', ''):
                pesq_return.send_keys(letra)
                sleep(random())
            sleep(1)
            pesq_return.send_keys(Keys.ENTER)

        except NoSuchElementException as er:
            driver.back()
            continue
        except Exception as erro:
            continue

driver.quit()
