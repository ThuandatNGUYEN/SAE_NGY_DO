#from csv_ical import Convert
import csv
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
import openpyxl

#Ouverture du fichier RTE_2020.csv
Liste_calendar=[]
with open('ADECal.csv',newline='') as csvfile: 
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        Liste_calendar.append(row)

#idexation 
idexation=["CM","TD","TP"]

#----------------------------------------------------------------------------------------

def tableau(liste_heure,index,colonne) :
    df = pd.DataFrame(liste_heure,index=index, columns=colonne) #liste_heure est une liste de liste
    #df.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')
    return df

#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33
#----------------------------------------------------------------------------------------
def classes(liste):
    for element in liste :
        if type(element) == list :
            None

print(type(Liste_calendar[1][3]))
#----------------------------------------------------------------------------------------


dico_prof=[]
for element in Liste_calendar :
    if element[5] in  dico_prof :
        None
    else :
        dico_prof += [element[5]]
        
#print(dico_prof)

def calc_heures(debut, fin):
    dt = datetime.strptime(debut, '%Y-%m-%d %H:%M:%S%z')
    fn = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S%z')
    difference = fn - dt
    return difference.total_seconds() / 3600

def par_mois(liste_date,choix) :

    liste_heures_par_mois = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    for element in Liste_calendar :
    
         if element[4] == choix:
            dt = datetime.strptime(element[1], '%Y-%m-%d %H:%M:%S%z')
            nb = dt.month()
            heures += calc_heures(element[1], element[2])
            liste_heures_par_mois[nb] = liste_heures_par_mois[nb] + heures 
    
    return liste_heures_par_mois

#choix = str(input("Choisissez un professeur: "))

Liste_calendar_mod = Liste_calendar

del Liste_calendar[0]

heures = 0
#for element in Liste_calendar:
    #if element[4] == choix:
       #heures += calc_heures(element[1], element[2])
#print(heures)


