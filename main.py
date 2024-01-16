import csv
import os
from datetime import datetime

import matplotlib.pyplot as plt
from openpyxl import Workbook


def load_data(file_path, delim=','):
    # fonction pour charger les fichiers.
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        temp = [[cell for cell in row] for row in reader]
    del temp[0]
    return temp


def get_uniq_sorted(index, boost="NOOP"):
    # récupérer une liste d'élément qui ne contiens pas de doublons.
    global donnees
    uniq = set()
    for elem in donnees:
        if elem[index] not in uniq and elem[index] and (boost == "NOOP" or boost in elem):
            uniq.add(elem[index])
    return sorted(list(uniq))


def calc_heures(debut, fin):
    # calculer le temps écoulé entre la fin et le début.
    dt = datetime.strptime(debut, '%Y-%m-%d %H:%M:%S%z')
    fn = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S%z')
    difference = fn - dt
    return difference.total_seconds() / 3600


def get_list_from_str(stlist, tolist=True):
    # récupérer la liste des salles depuis une liste en STRING.
    clean = stlist.replace('[', '').replace(']', '').replace("'", '')
    return clean.split(',') if tolist else clean


def get_type_from_room(room):
    # récupérer le type de salle depuis son nom.
    if "Amphi" in room:
        return "CM"
    elif "TD" in room:
        return "TD"
    return "TP"


# charge les données CSV dans les variables.
donnees = load_data('ADECal.csv')

choix = input("1: Professeur | 2: Module : ")

if choix == "1":
    datalist = get_uniq_sorted(4)
    print(datalist)
    enseignant = str(input("Choisissez un professeur dans la liste: "))
    if enseignant.isdigit() and len(datalist) >= int(enseignant):
        enseignant = datalist[int(enseignant) - 1]
        print("Vous avez sélectionné", enseignant)
    elif enseignant not in datalist:
        raise ValueError("Ce professeur n'existe pas.")
    datalist = get_uniq_sorted(0, enseignant)
    if len(datalist) == 0:  # ce n'est pas prêt d'arriver.
        print("Il semble que ce professeur n'ait pas été assigné à un module. Ses statistiques sont donc nulles.")
        exit(0)
    print(datalist)
    module = str(input("Choisissez un module dans la liste: "))
else:
    datalist = get_uniq_sorted(0)
    print(datalist)
    module = str(input("Choisissez un module dans la liste: "))
    if module.isdigit() and len(datalist) >= int(module):
        module = datalist[int(module) - 1]
    elif module not in datalist:
        raise ValueError("Ce module n'existe pas.")
    datalist = get_uniq_sorted(4, module)
    enseignant = ""
    if len(datalist) == 0:
        print(
            "Il semblerait que ce module ne comporte aucun professeur. Une statistique des salles est toujours possible.")
    else:
        print(datalist)
        enseignant = str(input("Choisissez un professeur dans la liste: "))

# Génération de l'Histogramme
labels = ["CM", "TD", "TP"]
mat_dict = {"CM": 0, "TD": 0, "TP": 0}

for element in donnees:
    if element[4] == enseignant and element[0] == module:
        mat_dict[get_type_from_room(element[5])] += calc_heures(element[1], element[2])

values = [mat_dict[label] for label in labels]
plt.figure(figsize=(10, 5))
plt.bar(labels, values)
plt.xlabel('Types de cours')
plt.ylabel('Heures accumulées')
plt.title('Histogramme des heures de ' + module + ' par ' + enseignant)
plt.show()

# Génération du tableau CSV & du tableau Excel (xlsx) dans un répertoire

repertoire = "tableaux générés"

if not os.path.exists(repertoire):
    os.makedirs(repertoire)

csv_path = os.path.join(repertoire, f"{enseignant} - {module.replace(':', '')}.csv")
xlsx_path = os.path.join(repertoire, f"{enseignant} - {module.replace(':', '')}.xlsx")

wb = Workbook()
ws = wb.active
ws.append(['Heure(s)', 'Type', 'Salle', 'Groupe'])
with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Heure', 'Type', 'Salle', 'Groupe'])

    for element in donnees:
        if element[4] == enseignant and element[0] == module:
            heure = calc_heures(element[1], element[2])
            salle = element[5]
            type_cours = get_type_from_room(salle)
            groupe = get_list_from_str(element[3], False)
            csv_writer.writerow([heure, type_cours, salle, groupe])
            ws.append([heure, type_cours, salle, groupe])

wb.save(xlsx_path)
