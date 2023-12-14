import csv
from datetime import datetime

import matplotlib.pyplot as plt


# fonction pour charger les fichiers.
def load_data(file_path, delim):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        temp = [[cell for cell in row] for row in reader]
    del temp[0]
    return temp


def get_uniq(index, boost="NOOP"):
    global donnees
    uniq = set()
    for elem in donnees:
        if elem[index] not in uniq and elem[index] and (boost == "NOOP" or boost in elem):
            uniq.add(elem[index])
    return list(uniq)


def calc_heures(debut, fin):
    dt = datetime.strptime(debut, '%Y-%m-%d %H:%M:%S%z')
    fn = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S%z')
    difference = fn - dt
    return difference.total_seconds() / 3600


def get_list_from_str(stlist):
    return stlist.replace('[', '').replace(']', '').replace("'", '').split(',')


def get_type_from_room(room):
    if "Amphi" in room:
        return "CM"
    elif "TD" in room:
        return "TD"
    return "TP"


# charge les données CSV dans les variables.
donnees = load_data('ADECal.csv', ',')

ens = get_uniq(4)
print(ens)
enseignant = str(input("Choisissez un professeur dans la liste: "))
if enseignant not in ens:
    raise ValueError("Ce professeur n'existe pas.")
matieres = get_uniq(0, enseignant)
print(matieres)
module = str(input("Choisissez un module dans la liste: "))

labels = ["CM", "TD", "TP"]
mat_dict = {"CM": 0, "TD": 0, "TP": 0}
for element in donnees:
    if element[4] == enseignant and element[0] == module:
        mat_dict[get_type_from_room(element[5])] += calc_heures(element[1], element[2])
        print(get_list_from_str(element[3]))

values = [mat_dict[label] for label in labels]
plt.figure(figsize=(7, 5))
plt.bar(labels, values)
plt.xlabel('Types de cours')
plt.ylabel('Heures accumulées')
plt.title('Histogramme des heures de cours par type')
plt.show()
