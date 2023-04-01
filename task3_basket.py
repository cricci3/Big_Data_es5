import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

teams = ['1538/banco-di-sardegna-sassari','1540/bertram-yachts-derthona-tortona','1534/carpegna-prosciutto-pesaro','1539/dolomiti-energia-trentino',
         '1533/ea7-emporio-armani-milano', '1532/germani-brescia','1535/gevi-napoli-basket','1537/givova-scafati',
         '1531/happy-casa-brindisi','1542/nutribullet-treviso-basket','1543/openjobmetis-varese','1541/pallacanestro-trieste',
         '1545/tezenis-verona','1544/umana-reyer-venezia','1536/unahotels-reggio-emilia','1530/virtus-segafredo-bologna']

cognomi = []
altezze = []
pesi = []

file_dati = open('dati_serieA.txt', 'w')

path = 'C:\\Program Files\\ChromeDriver\\chromedriver.exe'

for team in teams:
    website = f'https://www.legabasket.it/lba/squadre/2022/{team}'

    # Crea Driver
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(website)
    except:
        print(f'ERRORE; {website} non raggiungibile')

    time.sleep(1)
    try:
        cookie_btn = driver.find_element(By.XPATH, '//button[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        cookie_btn.click()
    except:
        pass
    time.sleep(0.5)

    RIGA_PLAYER = '//table[@class="table table-hover align-middle text-center table-team"]/tbody/tr'
    player_data = driver.find_elements(By.XPATH, RIGA_PLAYER)

    for player in player_data:
        if player.find_element(By.XPATH, '//td[8]').text == 'ITA':
            altezza_giocatore = player.find_element(By.XPATH,'//td[6]').text
            altezze.append(int(altezza_giocatore))

            peso_giocatore = player.find_element(By.XPATH,'//td[7]').text
            pesi.append(int(peso_giocatore))

            cognome = player.find_element(By.XPATH, '//td[3]/a/span').text
            cognomi.append(cognome)
            print(cognome+' '+str(altezza_giocatore)+ ' '+str(peso_giocatore))


    driver.close()

file_dati.write('\n'.join(cognomi) + '\n')
file_dati.write('\n'.join(altezze) + '\n')
file_dati.write('\n'.join(pesi) + '\n')