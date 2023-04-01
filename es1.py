import random
import matplotlib.pyplot as plt

# Calcolo i valori delle persone sottopeso
altUP = []
pesiUP = []
for n in range(0, int(100000 * 0.029)):
    alttmp = random.uniform(1.5, 2.15)
    pesotmp = random.uniform(16, 18.5) * (alttmp ** 2)
    altUP.append(alttmp)
    pesiUP.append(pesotmp)

# Calcolo i valori delle persone normopeso
altNP = []
pesiNP = []
for n in range(0, int(100000 * 0.509)):
    alttmp = random.uniform(1.5, 2.15)
    pesotmp = random.uniform(18.5, 25) * (alttmp ** 2)
    altNP.append(alttmp)
    pesiNP.append(pesotmp)

# Calcolo i valori delle persone sovrappeso
altOP = []
pesiOP = []
for n in range(0, int(100000 * 0.3420)):
    alttmp = random.uniform(1.5, 2.15)
    pesotmp = random.uniform(25, 30) * (alttmp ** 2)
    altOP.append(alttmp)
    pesiOP.append(pesotmp)

# Calcolo i valori delle persone obese
altO = []
pesiO = []
for n in range(0, int(100000 * 0.12)):
    alttmp = random.uniform(1.5, 2.15)
    pesotmp = random.uniform(30, 35) * (alttmp ** 2)
    altO.append(alttmp)
    pesiO.append(pesotmp)

f1 = plt.figure(1)
plt.title('Distribuzione BMI popolazione italiana')
plt.scatter(pesiUP, altUP, color='yellow', label='Sottopeso')
plt.scatter(pesiNP, altNP, color='red', label='Normopeso')
plt.scatter(pesiOP, altOP, color='green', label='Sovrappeso')
plt.scatter(pesiO, altO, color='blue', label='Obeso')
plt.xlabel("Peso (KG)")
plt.ylabel("Altezza (m)")
plt.legend()
plt.show()


altezzeSottoP = []
pesiSottoP = []

altezzeNP = []
pesiNP = []

altezzeSP = []
pesiSP = []

altezzeO = []
pesiObesi =  []

# Altezza e peso di tutti i giocatori italiani di Serie A basket, i dati sono stati presi da https://www.legabasket.it/lba/3/squadre
altezze = [206, 196, 204, 188, 191, 198, 204, 208, 185, 190, 188, 190, 204, 196, 198, 190, 192, 200, 205, 211, 181, 194,
           196, 195, 188, 199, 200, 200, 207, 108, 194, 206, 202, 200, 192, 200, 203, 180, 194, 184, 203, 194, 187, 203,
           205, 200, 175, 192, 208, 193, 207, 190, 192, 185, 190, 207, 196, 188, 192, 195, 206, 196, 191, 180, 206, 198,
           208, 190, 205, 198, 205, 208, 183, 186, 205, 196, 193, 198, 199, 205, 185, 194, 185, 188, 203, 203, 194, 207,
           198, 196, 191, 193, 206, 190, 191, 196, 194, 197, 208, 214, 198]
pesi = [110, 96, 105, 80, 95, 91, 100, 105, 72, 86, 82, 85, 95, 88, 84, 81, 87, 90, 107, 98, 78, 90, 84, 89, 85, 88,
        104, 89, 95, 108, 100, 107, 102, 106, 88, 92, 101, 73, 90, 81, 110, 90, 83, 96, 105, 96, 70, 84, 106, 80, 106,
        85, 86, 78, 85, 98, 90, 78, 92, 92, 113, 89, 79, 70, 92, 97, 90, 90, 90, 90, 105, 104, 80, 82, 85, 90, 88, 105,
        85, 100, 81, 103, 75, 91, 103, 100, 92, 100, 100, 86, 90, 85, 105, 86, 84, 100, 95, 96, 95, 114, 98]

numero_dati = len(altezze)
print(numero_dati)
print(len(pesi))

for i in range(numero_dati):
    altezza = altezze[0]
    peso = pesi[0]

    print(str(altezza) + ' ' + str(peso))
    bmi = peso/((altezza/100)**2)
    if bmi <= 18.4:
        altezzeSottoP.append(altezza)
        pesiSottoP.append(peso)
        print('sottopeso: '+str(bmi))
    elif bmi > 18.4 and bmi <= 24.9:
        altezzeNP.append(altezza)
        pesiNP.append(peso)
        print('normopeso: '+str(bmi))
    elif bmi > 24.9 and bmi <= 30:
        altezzeSP.append(altezza)
        pesiSP.append(peso)
        print('sovrappeso: '+str(bmi))
    else:
        altezzeO.append(altezza)
        pesiObesi.append(peso)
        print('obeso: '+str(bmi))
    print()

    del altezze[0]
    del pesi[0]


print('sono state prese in considerazione: '+str(len(altezzeSottoP) + len(altezzeNP) + len(altezzeSP) + len(altezzeO))+' altezze')
print('sono state prese in considerazione: '+str(len(pesiSottoP) + len(pesiNP) + len(pesiSP) + len(pesiObesi))+' pesi')

f2 = plt.figure(2)
plt.title('Distribuzione BMI cestiti italiani di Serie A')
plt.scatter(pesiSottoP, altezzeSottoP, color='yellow', label='Sottopeso')
plt.scatter(pesiNP, altezzeNP, color='red', label='Normopeso')
plt.scatter(pesiSP, altezzeSP, color='green', label='Sovrappeso')
plt.scatter(pesiObesi, altezzeO, color='blue', label='Obeso')
plt.xlabel("Peso (KG)")
plt.ylabel("Altezza (m)")
plt.legend()
plt.show()
