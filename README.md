# Conversion d'un fichier iCalendar en fichier CSV

Le script Python "converter.py" permet de convertir un fichier au format iCalendar (ICS) en un fichier CSV. Il extrait les informations pertinentes des événements du calendrier et les stocke dans un fichier CSV pour une utilisation plus conviviale.

# Installation des dépendances

Assurez-vous d'installer les dépendances nécessaires en exécutant la commande suivante:

    pip install icalendar

# Analyse de Données

Le script Python "main.py" est conçu pour analyser les données extraites d'un fichier CSV généré à partir des données sortie du convertisseur. Il offre des fonctionnalités de traitement de données, de génération d'histogrammes et de création de tableaux CSV et Excel pour des statistiques détaillées.

# Installez les dépendances nécessaires en exécutant la commande suivante:

    pip install matplotlib openpyxl

# Utilisation

Placez le fichier CSV généré à partir du convertisseur dans le même répertoire que le script. Exécutez le script en utilisant la commande:

    (Linux)
    python3 main.py

    (Windows)
    py main.py

Suivez les instructions à l'écran pour sélectionner les statistiques que vous souhaitez générer.

L'histogramme des heures de cours sera affiché, et deux fichiers seront générés dans un répertoire appelé "tableaux générés":
        Enseignant - Module.csv: Tableau CSV avec les heures, types de cours, salles et groupes associés.
        Enseignant - Module.xlsx: Tableau Excel (xlsx) avec les mêmes informations que le fichier CSV.
