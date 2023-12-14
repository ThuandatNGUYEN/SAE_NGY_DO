import csv

from datetime import datetime


# fonction pour charger les fichiers.
def load_data(file_path, delim):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        temp = [[cell for cell in row] for row in reader]
    del temp[0]
    return temp


# charge les données CSV dans les variables.
donnees = load_data('ADECal.csv', ',')
print(donnees)

choix = str(input("Choisissez un professeur: "))


def calc_heures(debut, fin):
    dt = datetime.strptime(debut, '%Y-%m-%d %H:%M:%S%z')
    fn = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S%z')
    difference = fn - dt
    return difference.total_seconds() / 3600


heures = 0
for element in donnees:
    if element[4] == choix:
        heures += calc_heures(element[1], element[2])
print(heures)