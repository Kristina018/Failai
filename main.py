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

# with open('./Miestai.txt') as failas:
#     teksto_eilute = failas.readline()
# with open('./Miestu_kopija.txt', 'w') as miestai:
#     miestai.write(teksto_eilute)

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

# # 389 skaidre
# 3. Sukurkite du dictionary dviejų knygų informacijai saugoti. Kiekviename dictionary nurodykite tokias savybes su
# reikšmėmis: pavadinimas, autorius, žanras, kaina, puslapių kiekis, skyrių sąrašas (masyvas su pavadinimais),
# išleidimo metai, ar knygą galima rasti knygynuose. Išveskite šių knygų informaciją. Išveskite kuri knyga plonesnė
# (turi mažiau puslapių), bei kurioje knygoje yra daugiau skyrių. Paskaičiuokite, jeigu pigesnės knygos kainą
# padvigintumėte, ar ji jau būtų brangesnė už kitą knygą?

# # 390 skaidre
# 4. Sukurkite tris dictionary prekių duomenims saugoti. Kiekviename dictionary sudėkite šias savybes su reikšmėmis:
# pavadinimas, kaina, savikaina, kodas, turimas kiekis sandėlyje, siuntimui dėžės matmenys (x, y, z ašys).
# Išveskite visų trijų prekių informaciją. Išveskite visų prekių kainas vienoje eilutėje (pirma prekė kainuoja - ...,
# antra prekė kainuoja - ..., ir t.t.). Raskite ir išveskite kuri prekė yra brangiausia (jos pavadinimą ir kainą arba
# visą rastos prekės informaciją). Raskite ir išveskite atskirose eilutėse kiekvienos prekės dėžės tūrį.
# Raskite ir išveskite atskirose eilutėse kiekvienos prekės pelningumą ((kaina - savikaina) * kiekis sandėlyje).

# # 391 skaidre
# 5. Sukurkite dictionary automobilio duomenims saugoti. Į šį dictionary savybes su reikšmėmis sukelkite,
# po to kai sukursite tuščią dictionary (14- as pavyzdys). Sudėkite šias savybes su reikšmėmis:
# markė, modelis, rida, gamybos metai, spalva, darbinis tūris, ar daužta, ar parduodama.
# Išveskite visą automobilio informaciją. Paskaičiuokite ir išveskite kiek automobiliui yra metų
# (rankomis įrašykite dabartinius metus arba panaudokite datetime.date.today().year funkciją,
# pačiame failo viršuje reikės nurodyti import datetime). Paskaičiuokite ir išveskite kiek
# vidutiniškai per metus yra nuvažiavęs automobilis (jeigu viso nuvažiavo 300 kilometrų, o automobiliui yra 2 metai,
# tai per metus vidutiniškai gaunasi 150 km.).

# # 392 skaidre
# 6. Sukurkite savo norimą dictionary(-us). Kiekviename sudėkite bent 5 savybes su reikšmėmis
# (reikšmes galite įdėti ir atskirai). Išveskite informaciją. Pagalvokite ką dar galite su šiuo dictionary atlikti
# (paskaičiuoti ir pan.) ir tai padarykite.

# # # 410 skaidre
# # 7. Susikurkite dictionary informacijai apie knygyną saugoti. Į šį dictionary sudėkite tokias
# # savybes su reikšmėmis: pavadinimas, adresas, plotas (kv. m.), kiek turi knygų, darbo valandos,
# # ar atidarytas. Išveskite šio knygyno dictionary raktus su reikšmėmis.
# knygynas = {
#     "pavadinimas": 'Knygynelis',
#     "adresas": "Pylimo 16",
#     "plotas": 135,
#     "kiekis": 35000,
#     "darbo valandos": [8, 22],
#     "atidarytas": True
# }
# for raktas, value in knygynas.items():
#     print (raktas, value)


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
# if vidurkis2 > vidurkis1:
#     print(f'Vidurkis {vidurkis2} yra didesnis ir priklauso antram studentui:')
#     print(f'{studentas2['vardas']} {studentas2['pavardė']}.')
# else:
#     print(f'Vidurkis {vidurkis1} yra didesnis ir priklauso pirmam studentui:')
#     print(f'{studentas1['vardas']} {studentas1['pavardė']}.')

# # 411 skaidre
# 9. Susikurkite dictionary, kuriame būtų nurodytos prekės ir turimi kiekiai, t.y.
# raktas yra prekės pavadinimas ir reikšmė yra turimas prekės kiekis, o visa tai saugoma
# viename dictionary (panašu į 29 pavyzdį). Išveskite visą turimą dictionary informaciją
# gražiai suformatuotai, pvz: '- Prekės "Pieštukas" liko 132 vnt.'
# ir tai padaryti atskirose eilutėse. Taip pat, raskite ir išveskite visų prekių
# bendrą turimą kiekį (sudėti visus turimus kiekius), kiekių vidurkį
# (kiek vidutiniškai turima prekių). O tos prekės kurios likę mažiausiai vienetų
# išvesti pavadinimą ir kiekį.

# sumustiniai = dict(
#    batonas = 10,
#    sviestas = 12,
#    desra = 8.5,
#    suris = 8.3, # 8.3 - 8.4
#     antras_suris = 9,
#    pomidorai = 17.8,
#    plastikiniai_maiseliai = 2
# )
# for raktas, reiksme in sumustiniai.items():
#     print(f'Prekes \'{raktas}\' yra like {reiksme} vnt.')
#
# prekiu_suma = 0
# for reiksme in sumustiniai.values():
#     prekiu_suma += reiksme
# print(f'- Visu prekiu kiekis yra {prekiu_suma} vnt.')
#
# print(f'- Vidutiniskai prekiu kiekis yra {round(prekiu_suma/len(sumustiniai),2)} vieneto.')
#
# # print(f'- Maz vienetu yra {min(sumustiniai.values())} vnt. sios prekes: {sumustiniai.keys()}.')
#
#
# positions = [] # output variable
# min_value = float("inf")
# for k, v in sumustiniai.items():
#     if v == min_value:
#         positions.append(k)
#     if v < min_value:
#         min_value = v
#         positions = [] # output variable
#         positions.append(k)
# # print(positions)
#
# for i in positions:
#     print(f'- Maziausiai prekiu turi \'{i}\' - {min_value} vnt.')

# def minimums(some_dict):
#     positions = [] # output variable
#     min_value = float("inf")
#     for k, v in some_dict.items():
#         if v == min_value:
#             positions.append(k)
#         if v < min_value:
#             min_value = v
#             positions = [] # output variable
#             positions.append(k)
#
#     return positions

# # 412 skaidre
# 10.Susikurkite dictionary darbuotojo informacijai saugoti. Nurodykite tokias savybes:
# vardas ir pavardė, telefonas, profesija, etatas, atlyginimas. Taip pat, sukurkite dar vieną
# darbuotojo dictionary, tačiau nenurodykite 1-os ar 2-ų savybių, pvz, praleiskite profesiją.
# Parašykite tokią programą, kuri galėtų išsiaiškinti kurios(-ių) savybių nėra antrame dictionary,
# kurios yra pirmame, pvz jeigu nėra profesijos, tai programa išsiaiškintų,
# kad nėra nurodyta profesija antrame dictionary. Padarykite taip, kad vartotojas turėtų galimybę
# suvesti trūkstamas savybes.

employee1 = {
    'name': 'Gitanas',
    'surname': 'Nauseda',
    'phone': 860000001,
    'profession': 'President',
    'salary': 10000
}
employee2 = {
    'name': 'Ingrida',
    'phone': 860000002,
}
print(employee1)
print(employee2)

z = set(employee1) - set(employee2)
print(f'Toks yra skirtumas tarp raktu: {z}.')

for i in z:
    employee2[i] = input(f'Iveskite reiksme raktui \'{i}\': ')
    employee2.update({i: employee2[i]})
# print(employee2)

# print(employee1)
# print(employee2)

a = employee1.values()
b = employee2.values()

print(a)
print(b)


# x = employee2.keys()
# print(x) #before the change
# employee2["color"] = "white"
# print(x) #after the change
# print(employee2)

# keys1 = employee1.keys()
# print(keys1)
# keys2 = employee2.keys()
# print(keys2)

# x = employee2["salary"]
# print(x)
# y = employee2.get("salary")
# print(y)


# for d in darbuotojai:
#     for v in d:
#         print(d[v])

# for d in darbuotojai: # sprendimukas jei zodynai yra liste:
#     for v in d:
#         if d[v] != '':
#             print(v)
    # if darbuotojai[1]['pavarde'] == True)

# for i in darbuotojai:
#     print(i)

# for darbuotojas in darbuotojai:
#     print(f'- {darbuotojas['profesija']} {darbuotojas['vardas']} {darbuotojas['pavarde']}: '
#           f'tel. {darbuotojas['telefonas']}, '
#           f'gauna {darbuotojas['atlyginimas']} € algos uz {darbuotojas['etatas']} etata.')




# # 413 skaidre
# 11.Kaimynystėje yra trys kepyklos, apie kiekvieną yra žinoma ši informacija:
# pavadinimas; darbuotojų kiekis; adresas; praeitos savaitės iškeptų kepinių kiekiai
# (sąrašas su 7-iais elementais, kur nurodyti atskiri kepinių kiekiai).
# Susikurkite dictionaries kiekvienai kepyklai. Jeigu vienas kepinys parduodamas už 1.5 euro,
# raskite kuri kepykla galėjo būti pelningiausia. Taip pat, išsiaiškinkite kiek vidutiniškai
# kiekviena kepykla per dieną pagamina kepinių, raskite kurios kepyklos vidurkis mažiausias.

# kepykla1 = {
#     'pavadinimas': "Obelele",
#     'darbuotojų kiekis': 5,
#     'adresas': 'Obelu 1',
#     'praeita savaite iskepe': [1, 2, 3, 5, 10, 15, 30]
# }
# print(kepykla1)
#
# kepykla2 = {
#     'pavadinimas': "Aguonele",
#     'darbuotojų kiekis': 52,
#     'adresas': 'Aguonu 2',
#     'praeita savaite iskepe': [12, 24, 31, 59, 120, 195, 300]
# }
# print(kepykla2)
#
# kepykla3 = {
#     'pavadinimas': "Citrinele",
#     'darbuotojų kiekis': 35,
#     'adresas': 'Citrinu 3',
#     'praeita savaite iskepe': [34, 9, 16, 42, 111, 85, 150]
# }
# print(kepykla3)
#
# kepinys = 1.5



# # # 423 skaidre
# # 12.Susikurkite sąrašą, kuriame būtų saugomos skirtingos knygos (kaip dictionary elementai).
# # Apie kiekvieną knygą į atskirus knygų dictionary sudėkite norimą informaciją (bent 3 savybes).
# # Į list įdėkite bent 3 knygas. Visas šias knygas išsiveskite. Tuomet parodykite pirmą knygą.
# # Antros knygos kažkurią savybę.
# knygos = [
#     dict(autorius = "Markas Tvenas", knyga = "Tomo Sojerio nuotykiai", metai = 1876, salis='JAV'),
#     dict(autorius="Astrid Lindgren", knyga="Pepe Ilgakojine", metai=1945, salis='Svedija'),
#     dict(autorius="Isaac Asimov", knyga="Fondas", metai=1951, salis='JAV')
# ]
# for i in knygos:
#     print(i)
# print(f'Pirmoji knyga: {knygos[0]}.')
# print(f'Antros knygos salis: {knygos[1]['salis']}.')
# # x = knygos[0].keys() # isspausdina raktus
# # print(x)


# # 423 skaidre
# 13.Susikurkite sąrašą, kuriame būtų keletas prekių (kaip dictionary elementai) ir jį
# užpildykite pasirinktais duomenimis. Išveskite visų prekių pavadinimus su kainomis
# ir dar kokiais nors atributais atskirose eilutėse.

# # 424 skaidre
# 14.Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą automobilių
# (kaip dictionary elementai) ir užpildykite jį pasirinktais duomenimis.
# Išveskite kiekvieno automobilio pavadinimą, metus ir paskaičiuotą jo amžių
# (dabartiniai metai - gamybos metai).

# # 424 skaidre
# 15.Susikurkite sąrašą, kuriame būtų saugoma keleto įmonių duomenys (kaip dictionary elementai)
# ir jį užpildykite duomenimis. Išveskite kiekvienos įmonės informaciją atskirose eilutėse,
# gražiai suformatuotai (sakinio pavidalu ar pan.). Taip pat, ką nors paskaičiuokite
# iš turimų skaitinių duomenų (pvz.: vidutinis įmonės amžius, darbuotojų kiekis per visas įmones,
# bendras pelnas, ar pan.).

# # 425 skaidre
# 16.Susikurkite sąrašą, kuriame būtų saugoma informacija apie skirtingas ligonines
# (kaip dictionary elementai) ir užpildykite jį pasirinktais duomenimis.
# Išveskite ligoninių pavadinimus su adresais skirtingose eilutėse.
# Suskaičiuokite ką nors iš skaitinių jų duomenų, pvz.: bendrą lankytojų kiekį,
# bendrą ar vidutinį darbuotojų kiekį, ar pan.

# # 426 skaidre
# 17.Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą studentų
# (kaip dictionary elementai), kur apie kiekvieną studentą būtų žinoma ši informacija:
# vardas ir pavardė, amžius, pažymiai, studijų programa, kursas. Kiekvieną studentą išveskite taip:
# pirmoje eilutėje visi studento duomenys išskyrus jo pažymius, antroje eilutėje jo pažymiai,
# trečioje jo pažymių vidurkis su prierašu 'pažymių vidurkis'.
# Išvedus visus studentus dėkite brūkšnį (pvz.: -----) ir išveskite bendrą visų studentų pažymių
# vidurkį.

# # 427 skaidre
# 18.Susikurkite parduotuvės dictionary, kuriame būtų ši informacija:
# pavadinimas, adresas, darbuotojų kiekis, prekių sąrašas (kiekviena kaip dictionary elementas).
# Apie kiekvieną prekę parduotuvėje žinoma ši informacija: pavadinimas; kodas; kaina; savikaina;
# turimas kiekis. Išveskite parduotuvės bendrą informaciją, tuomet užrašą "prekės" ir
# atskirose eilutėse turimas prekes su kuria nors jų informacija
# (pvz.: pavadinimai, kainos ir turimi kiekiai). Galiausiai paskaičiuokite kiek iš viso parduotuvė
# turi visų prekių (sudėkite jų kiekius). Raskite ir išveskite kurios prekės turima daugiausiai,
# o kurios mažiausiai.

# # 428 skaidre
# 19.Sukurkite norimą sąrašą iš dictionary elementų su norimais duomenimis.
# Atlikite išvedimus ir pasirinktus skaičiavimus.

# # 440 skaidre
# 20.Susikurkite vieną ar kelis objektus ir išmėginkite visus prieš tai pamatytus dict metodus
# (clear, copy, update, fromkeys, pop, ...)


# # # 453 - TUPLES
# # 1. Susikurkite tuple iš studijų programos modulių pavadinimų.
# # Atspausdinkite šiuos pavadinimus sąraše, prieš kiekvieną pavadinimą išvedant brūkšniuką.
# # Raskite ilgiausią modulio pavadinimą.
#
# tuple1 = ('Duomenys', 'Analitika', 'Programavimas')
#
# for i in tuple1:
#     print(f'- {i} -')
#
# max = len(tuple1[0])
# for i in tuple1:
#     if len(i) > max:
#         max = len(i)
# print(f'Ilgiausia modulio pavadinima turi \'{i}\': {len(i)} zenklu!')

# # 453 skaidre - TUPLES
# 2. Susikurkite tuple iš mėnesių pavadinimų. Susikurkite kitus tuples sezonams apibūdinti:
# žiema, pavasaris, vasara, ruduo. Panaudokite slicing [start:end], kad atitinkamus mėnesius sudėtumėte
# į atitinkamus sezonų tuples. Šį priskyrimą turite atlikti kuriant individualius sezonų tuples,
# kitaip išmes klaidą, kad jo negalite modifikuoti.

# menesiai = ('Kovas', 'Balandis', 'Geguze', 'Birzelis', 'Liepa', 'Rugpjutis',
#             'Rugsejis', 'Spalis', 'Lapkritis', 'Gruodis', 'Sausis', 'Vasaris')
# menesiai2 = ('Sausis', 'Vasaris', 'Kovas', 'Balandis', 'Geguze', 'Birzelis',
#             'Liepa', 'Rugpjutis', 'Rugsejis', 'Spalis', 'Lapkritis', 'Gruodis')
#
# pavasaris = (menesiai[0:3])
# print(pavasaris)
#
# pavasaris2 = (menesiai[0:2], menesiai[11])
# print(pavasaris2)

# Rasos:
# winter = menesiai2[-1:] + menesiai2[0:2]
# print(winter)

# vasara = tuple(menesiai[3:6])
# ruduo = (menesiai[6:9])
# ziema = tuple(menesiai[9:12])
#
# print(vasara)
# print(ruduo)
# print(ziema)

# # Rolando sprendimas:
# menesiai = ('sausis', 'vasaris', 'kovas',
# 'balandis', 'geguze', 'birzelis', 'liepa',
# 'rugpjutis', 'rugsejis', 'spalis', 'lapkritis',
# 'gruodis')
#
# print(f'Spring: {menesiai[2:5]}')
# print(f'Summer: {menesiai[5:8]}')
# print(f'Autumn: {menesiai[8:11]}')
# print(f'Winter: {menesiai[11:12] + menesiai[0:2]}')

# # 478 skaidre --- SETS
# 1. Įsivaizduokite, kad sukūrėte balsavimo formą, kurioje žmogus galėjo rinktis 1 iš kelių galimų variantų
# (ar įrašyti savo) ir turite sąraše visus tuos balsavimo duomenis (pvz: balsavimui panaudotas klausimas
# “labiausiai patinkanti kalba:”,oatsakymai[‘c++’, ‘python’, ‘python’, ‘javascript’, ‘python’, ‘c#’, ‘javascript’]).
# Atrinkite visus skirtingus atsakymų variantus į atskirą sąrašą (būtų [‘c++’, ‘python’, ‘javascript’, ‘c#’]).

# # 478 skaidre --- SETS
# 2. Savo nuožiūra atlikite dar bent vieną analogišką užduotį.