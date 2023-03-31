import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

teams = ['atalanta', 'bologna-1', 'cremonese', 'empoli', 'fiorentina', 'verona', 'inter','juventus','lazio','lecce','milan',
        'monza','napoli','roma','salernitana','sampdoria','sassuolo','spezia','torino','udinese']

cognomi = []
altezze = []
pesi = []

file_dati = open('dati_serieA.txt', 'w')

path = 'C:\\Program Files\\ChromeDriver\\chromedriver.exe'

for team in teams:
    website = f'https://www.eurosport.it/calcio/squadre/{team}/teamcenter.shtml'

    # Crea Driver
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(website)
    except:
        print(f'ERRORE; {website} non raggiungibile')

    time.sleep(1)
    try:
        cookie_btn = driver.find_element(By.XPATH, '//div[@class="banner-actions-container"]/button[@id="onetrust-accept-btn-handler"]')
        cookie_btn.click()
    except:
        pass
    time.sleep(0.5)

    TAG_SQUADRA = '//span[@class="svg-icons svg-teamcompo"]'
    squadra_btn = driver.find_element(By.XPATH, TAG_SQUADRA)
    squadra_btn.click()

    time.sleep(0.5)

    player_data = driver.find_elements(By.XPATH, '//ul[@class="teamcompo__list"]/li/span')

    for player in player_data:




    for player in player_data:
        altezza_giocatore = ''
        peso_giocatore = ''
        nome = ''
        # Se è pari allora sono le informazioni di altezza e peso
        if player_data.index(player) % 2 == 0:
            altezza_giocatore = player.find_element(By.XPATH, '//span[@class="player_infos"][1]').text
            altezza_giocatore = altezza_giocatore.replace('m','')
            altezze.append(altezza_giocatore)

            peso_giocatore = player.find_element(By.XPATH, '//span[@class="player_infos"][2]').text
            peso_giocatore = peso_giocatore.replace('kg', '')
            pesi.append(peso_giocatore)

        # Se è dispari informazione nome
        else:
            bandiera = player.find_element(By.XPATH,'//img[@class="flag"]')
            # Se è italiano
            if bandiera.get_attribute('src') == 'src="https://i.eurosport.com/_iss_/geo/country/flag/small/2210.png"':
                # Prendi nome
                nome = player.find_element(By.XPATH, '//a[@class="player_name"]').text
                nome = nome.replace('&nbsp',' ')
                cognomi.append(nome)
            else:
                pass

        print(team + ' ' + nome + ' '+ altezza_giocatore + ' '+ peso_giocatore)

    driver.close()

file_dati.write('\n'.join(cognomi) + '\n')
file_dati.write('\n'.join(altezze) + '\n')
file_dati.write('\n'.join(pesi) + '\n')