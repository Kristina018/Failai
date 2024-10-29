### --- 2024 spalio 21, pirmadienis --- 1. dalis --- C R U D --- ###
### --- 2024 spalio 21, pirmadienis --- 1. dalis --- C R U D --- ###
### --- 2024 spalio 21, pirmadienis --- 1. dalis --- C R U D --- ###
from itertools import count

# import datetime
#
# galimybes = [
#     [
#         'Jonas',
#         'ligonine',
#         datetime.datetime(2024, 10, 21, 12, 00, 0),
#         datetime.datetime(2024, 10, 21, 17, 00, 0)
#     ],
#     [
#         'Vilma',
#         'kriziu centras',
#         datetime.datetime(2024, 10, 21, 7, 00, 0),
#         datetime.datetime(2024, 10, 21, 12, 00, 0)
#     ],
#     [
#         'Laimis',
#         'skyrius',
#         datetime.datetime(2024, 10, 21, 17, 00, 0),
#         datetime.datetime(2024, 10, 21, 22, 00, 0)
#     ],
#     [
#         'Asta',
#         'ligonine',
#         datetime.datetime(2024, 10, 21, 22, 00, 0),
#         datetime.datetime(2024, 10, 22, 7, 00, 0)
#     ]
# ]
#
# def printInfo():
#     print("1. galimybiu sarasas 2. ideti 3. redaguoti 4. trinti 5. baigti programa")
#     # print('1. galimybes atvaizdavimas')
#     # print('2. naujos galimybes ikelimas')
#     # print('3. galimybes redagavimas')
#     # print('4. galimybes salinimas')
#     # print('5. iseiti is programos')
#
# printInfo()
#
# def printGalimybe(galimybe, num = 1):
#     print(f'{num}. {galimybe[0]} gali budeti @{galimybe[1]} nuo {galimybe[2]} '
#           f'iki {galimybe[3]}. \t Numatoma trukme butu {galimybe[3]-galimybe[2]} valandos.')
#
# def printGalimybes():
#     num = 1
#     for galimybe in galimybes:
#         printGalimybe(galimybe, num)
#         num += 1
#
# def addGalimybe():
#     print('Koks savanorio vardas?')
#     galimybeVardas = input()
#     print('Kur gali butdeti?')
#     galimybeVieta = input()
#     print('Kada gali pradeti? (yyyy-mm-dd hh:mm:ss)')
#     galimybePradzia = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
#     print('Kada noretu eit namo? (yyyy-mm-dd hh:mm:ss)')
#     galimybePabaiga = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
#     galimybes.append([galimybeVardas, galimybeVieta, galimybePradzia, galimybePabaiga])
#
# def editGalimybe():
#     print('Iveskite savanorio numeri, kurio galimybe noresit redaguoti:')
#     ed = int(input())
#     printGalimybe(galimybes[ed-1])
#     print('Suveskite naujas reiksmes:')
#     print('Kas keicia savo laikus?')
#     galimybeVardas = input()
#     print('Kur gali budeti?')
#     galimybeVieta = input()
#     print('Kada gali pradeti? (yyyy-mm-dd hh:mm:ss)')
#     galimybePradzia = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
#     print('Kada noretu eit namo? (yyyy-mm-dd hh:mm:ss)')
#     galimybePabaiga = datetime.datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
#     galimybes[ed-1] = [galimybeVardas, galimybeVieta, galimybePradzia, galimybePabaiga]
#
# def removeGalimybe():
#     print('Iveskite savanorio numeri, kurio galimybe norite salinti')
#     rem = int(input())
#     galimybes.pop(rem-1)
#
# print("---Savanoriu galimybes---")
#
# while True:
#     printInfo()
#     opt = int(input())
#     match opt:
#         case 1:
#             printGalimybes()
#         case 2:
#             addGalimybe()
#             printGalimybes()
#         case 3:
#             editGalimybe()
#             printGalimybes()
#         case 4:
#             removeGalimybe()
#             printGalimybes()
#         case 5:
#             print("vardas ar vieta?")
#             kas = input()
#             print("Ko ieskai?")
#             ko = input()
#
#             print("opt a")
#             if kas == "vardas":
#                 print("prafiltravau pagal varda")
#             if kas == "vieta":
#                 print("prafiltravau pagal vieta")
#
#             print("opt b")
#             match kas:
#                 case "vardas":
#                     print()
#                 case "vieta":
#                     print()
#         case 6:
#             exit(1)
#
# def filterGalimybe():
#     if kas == 'vardas':



### --- 2024 spalio 21, pirmadienis --- 1. dalis --- T E X T --- ###
### --- 2024 spalio 21, pirmadienis --- 1. dalis --- T E X T --- ###
### --- 2024 spalio 21, pirmadienis --- 1. dalis --- T E X T --- ###


# 504
# 1. Susikurkite vieną keletą failų, pamėginkite juos nuskaityti taikant įvairas metodikas
# (viską vienu metu, po atskirą eilutę, sudedant į dictionary, ir pan.).

# open('Kristina.txt')
# failas = open('./Kristina.txt')
# nuskaitytas_tekstas = failas.read()
# print(nuskaitytas_tekstas)
# print()
#
# failas.seek(0)
# failas2 = open('./Metai.txt')
# nuskaitytas_tekstas2 = failas2.read()
# print('Nuskaitytas: ', nuskaitytas_tekstas2)

# failas.close()
# print(failas.closed())
# koks nors
# mano norimas

# failas = open('./Miestai.txt')
# failas.read()
# failas.close()
# print(failas.closed)

# with open('./Miestai.txt') as failas:
#     failas.read()
# print(failas.closed)

# with open('./Miestai.txt') as failas:
#     eilute = failas.readline()
#     print(eilute)

# with open('./Miestai.txt') as failas:
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)
#     eilute = failas.readline()
#     print(eilute)

# with open('./Miestai.txt') as failas:
#     visas_tekstas = failas.readlines()
#     print(visas_tekstas)

with open('./Miestai.txt') as failas:
    teksto_eilute = failas.readline()
with open('./Miestu_kopija.txt', 'w') as miestai:
    miestai.write(teksto_eilute)
# with open('./Miestu_kopija.txt', 'a') as miestai:
#
#     print(miestai)

# with open('./Miestai.txt') as failas:
#     visas_tekstas = failas.readlines()
#     print('Visas tekstas: ', visas_tekstas)
#     sutvarkytas_tekstas = [eilute[:-1] for eilute in visas_tekstas]
#     print('Sutvarkytas tekstas: ', sutvarkytas_tekstas)

# with open('./Miestai.txt') as failas:
#     visas_tekstas = failas.readlines()
#     print('Visas tekstas: ', visas_tekstas)
#     sutvarkytas_tekstas = [eilute.rstrip('\n') for eilute in visas_tekstas]
#     print('Sutvarkytas tekstas: ', sutvarkytas_tekstas)

# with open('./Miestai.txt') as failas:
#     tekstas = failas.read().splitlines()
#     print('Tekstas: ', tekstas)

# with open('./Miestai.txt') as failas:
#     print(type(failas.read()))
#     failas.seek(0)
#     print(type(failas.readline()))
#     failas.seek(0)
#     print(type(failas.readlines()))

# eilutes = []
# with open('./Miestai.txt') as failas:
#     while True:
#         eilute = failas.readline().rstrip('\n')
#         if not eilute:
#             break
#         print('nuskaityta eilute: ', eilute)
#         eilutes.append(eilute)
# print(eilutes)

# eilutes = []
# with open('./Miestai.txt') as failas:
#     for eilute in failas:
#         eilute = eilute.rstrip('\n')
#         print('nuskaityta eilute: ', eilute)
#         eilutes.append(eilute)
# print(eilutes)

# zmones = []
# with open('./zmones.txt', encoding = 'utf8') as failas:
#     for eilute in failas:
#         eilute = eilute.rstrip('\n')
#         isskaidyta = eilute.split(';')
#         zmogus = dict(
#             vardas = isskaidyta[0],
#             pavarde = isskaidyta[1],
#             amzius = isskaidyta[2],
#             miestas = isskaidyta[3],
#             numeris = isskaidyta[4]
#         )
#         zmones.append(zmogus)
# print(zmones)

# with open('./Miestai.txt') as failas:
#     print(type(failas.read()))
#     failas.seek(0)
#     print(type(failas.readline()))
#     failas.seek(0)
#     print(type(failas.readlines()))

# with open('./rasymui.txt', "w") as failas:
#     failas.write('pirma\n')
#     failas.write('antra ' * 10)
# print(failas)

# with open('./rasymui2.txt', 'w') as failas:
#     failas.write('pirma\t')

# failas = open('./rasymui2.txt', 'w')
# failas.write('antra\n')
# failas.write('trecia\n')
# failas.close()

# with open('./rasymui10.txt', 'w') as failas:
#     failas.write('labas rytas\n')
# with open('./rasymui10.txt', 'a') as failas:
#     failas.write('daugiau teksto\n')
# with open('./rasymui10.txt', 'a') as failas:
#     failas.write('siek tiek kito teksto\n')
# with open('./rasymui10.txt', 'r+') as failas: # istrina pirma eilute ir ant jos uzraso savo nauja teksta
#     failas.write('dar teksto\n' * 2)
#     failas.write('ir dar daugiau ' * 2)

# with open('./rasymui7.txt', 'w') as failas:
#     failas.write('tekstas')
# with open('./rasymui7.txt', 'r+') as failas:
#     failas.write(':)' * 10)
#     failas.seek(10)
#     failas.write('na va')


# 514
# 2. Pamėginkite išvesti skirtingą informaciją į keletą atskirų failų.
# Tiek perrašant kas yra tame faile, tiek bandant jį papildyti.
# Galite išvesti kokių nors skaičiavimų informaciją.
# auksciau pavyzdziuose ta padariau (tik ne skaiciavimus...)

# # 3. Susikurkite duomenų failą, iš kurio nusiskaitytumėte informaciją apie automobilius.
# # Išskaičiuokite keletą norimų dalykų (pvz. metų vidurkį)
# # ir skaičiavimų rezultatus išveskite rezultatų faile.
# zmones = []
# with open('./zmones.txt', encoding = 'utf8') as failas:
#     for eilute in failas:
#         eilute = eilute.rstrip('\n')
#         isskaidyta = eilute.split(';')
#         zmogus = dict(
#             vardas = isskaidyta[0],
#             pavarde = isskaidyta[1],
#             amzius = isskaidyta[2],
#             miestas = isskaidyta[3],
#             numeris = isskaidyta[4]
#         )
#         zmones.append(zmogus)
# # print(zmones)
# with open('./rezultatai.txt', 'w') as rezultatai:
#     amziai = []
#     for i in amzius:
#         amziai.append(isskaidyta)
# print(amziai)

# 524
# 4. Susikurkite pasirinktą csv failą ir užpildykite jį duomenimis.
# Pamėginkite jį nuskaityti su reader ir su DictReader.
# Iš šio failo duomenų išsiskaičiuokite bent 2 pasirinktus dalykus
# (pvz studentų vidurkių vidurkį, rasti žemiausią studentą, ar pan.).
# Nuskaitytus duomenis ir gautus rezultatus išveskite ekrane.

# 5. Pasikurkite kitą csv failą, su kitais duomenimis. Pamėginkite nuskaityti šį failą pasirinktu būdu.
# Išsiskaičiuokite iš šio failo norimus dalykus. Išveskite pradinius duomenis ir gautus rezultatus.

# 531
# 6. Susikurkite norimą csv failą su duomenimis. Nuskaitykite šį failą pasirinktu būdu.
# Paskaičiuokite ar raskite iš šio failo duomenų bent 3 skirtingus dalykus
# (geriausiai besimokantį studentą, aukščiausią studentą, mažiausią vidurkį, ...).
# Gautus rezultatus išveskite į atskirą failą (galite tiesiog txt failą).

# 7. Susikurkite norimą csv failą su duomenimis. Nuskaitykite šio failo duomenis pasirinktu būdu.
# Atfiltruokite duomenis pagal pasirinktą kriterijų (pvz, visus studentus, kurių vidurkis didesnis nei 8)
# ir šiuos atfiltruotus duomenis išspausdinkite į atskirą csv failą.

# # 1. Sukurkite dictionary studento duomenims saugoti.
# # Į šį dictionary sudėkite tokias savybes su reikšmėmis:
# # vardas, pavardė, amžius, studijų programa, atsiskaitytų kreditų skaičius, pažymiai,
# # amžius, ūgis, kelintame kurse mokosi, kurioje mokykloje mokosi.
# # Šiuos duomenis galite grupuoti į vidinius dictionary arba visus išrašyti atskirai.
# # Išveskite šią informaciją per vieną print(). Taip pat, pamėginkite išvesti atskirose
# # eilutėse tris skirtingas pasirinktas savybes.
#
# studentas = {
#     'vardas': 'Jonas',
#     'pavardė': 'Jonauskas',
#     'studijų_programa': 'Duomenu analitika',
#     'atsiskaitytų_kreditų_skaičius': 5,
#     'pažymiai': [9, 8, 10, 7, 9],
#     'amžius': 23,
#     'ūgis': 180,
#     'kursas': 1,
#     'mokykla': "VCS"
# }
# # print(studentas)
# print(studentas['vardas'])
# print(studentas['pažymiai'])
# print(studentas['mokykla'])



# # 2. Sukurkite dictionary informacijai apie filmą saugoti. Į šį dictionary sudėkite tokias savybes
# # su reikšmėmis: pavadinimas, režisierius, biudžetas, kiek uždirbo pinigų po išleidimo, žanras,
# # trukmė, išleidimo metai, aktorių sąrašas (masyvas su jų vardais ir pavardėmis).
# # Išveskite šio dictionary informaciją. Paskaičiuokite ir išveskite šio filmo pelną
# # (uždarbis - biudžetas). Išveskite kiek filme dalyvavo aktorių (jų kiekis).
# # Paskaičiuokite kiek filmui yra metų (dabartinius metus tiesiog galite įrašyti rankomis
# # arba panaudoti datetime.date.today().year funkciją, pačiame failo viršuje reikės nurodyti import datetime).
#
# import datetime
# filmas = {
#     'pavadinimas': 'Titanic',
#     'režisierius': 'Režisierius',
#     'biudžetas': 1000000,
#     'uždarbis': 50000000,
#     'žanras': 'drama',
#     'trukmė': 201,
#     'metai': 1997,
#     'aktoriai': ["Kate Winslet", "Leonardo DiCaprio", "Trečias aktorius", "Antraplanis", "Trečiaplanis"],
# }
# # print(filmas)
# print(f'Titaniko pelnas yra {filmas['uždarbis'] - filmas['biudžetas']}.')
# print(f'Filme vaidino {len(filmas['aktoriai'])} aktoriai.')
# print(f'Nuo pastatymo praėjo {datetime.date.today().year - filmas['metai']} metai.')

# # 410 skaidre
# # 8. Susikurkite du dictionary, dviejų studentų informacijai saugoti.
# # Abiejuose dictionary sudėkite šias savybes su reikšmėmis:
# # vardas ir pavardė, studijų programos pavadinimas, pažymiai.
# # Raskite abiejų studentų pažymių vidurkius. Išveskite abiejų studentų informaciją,
# # bei pažymių vidurkius. Raskite ir išveskite, kurio studento pažymių vidurkis yra didesnis ir
# # išveskite jo vardą su pavarde.
#
# studentas1 = {
#     'vardas': 'Jonas',
#     'pavardė': 'Jonauskas',
#     'studijų_programa': 'Duomenu analitika',
#     'pažymiai': [9, 8, 10, 7, 9],
# }
#
# studentas2 = {
#     'vardas': 'Kostas',
#     'pavardė': 'Kostauskas',
#     'studijų_programa': 'Duomenu analitika',
#     'pažymiai': [10, 7, 9, 6, 5],
# }
#
# suma1 = 0
# for i in studentas1['pažymiai']:
#     suma1 += i
# vidurkis1 = suma1 / len(studentas1['pažymiai'])
#
# suma2 = 0
# for i in studentas2['pažymiai']:
#     suma2 += i
# vidurkis2 = suma2 / len(studentas2['pažymiai'])
#
# # print(studentas1)
# print(f'Pirmo studento pažymių vidurkis yra {vidurkis1}, o antro - {vidurkis2}.')
# print()


# if vidurkis2 > vidurkis1:
#     print(f'Antro studento vidurkis {vidurkis2} yra didesnis uz pirmojo, kuris yra {vidurkis1}.')
# else:
#     print(f'Pirmo studento vidurkis {vidurkis1} yra didesnis uz pirmojo, kuris yra {vidurkis2}.')