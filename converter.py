import csv

from icalendar import Calendar


def ics_to_csv(ics_file, csv_file):
    with open(ics_file, 'rb') as ics_file:
        # Ouverture du calendrier
        cal = Calendar.from_ical(ics_file.read())

        # Ouvrir le csv en écriture
        with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            # Écriture de la première ligne "header'
            writer.writerow(['Matière', 'Heure de début', 'Heure de fin', 'Groupe(s)', 'Professeur', 'Salle'])

            # Iteration du calendrier
            for event in cal.walk('VEVENT'):
                # Extraction des informations
                summary = str(event.get('summary')).replace('\n', ',')
                description = str(event.get('description')).replace('\n', ',')
                location = str(event.get('location')).replace('\n', ',')

                # Traitement de la description
                desc = [item.strip() for item in description.split(',') if "Exported" not in item and item != ""]
                prof = desc[-1] if len(desc) > 1 and desc[-1][:2] != "RT" else ""
                desc = desc[:-1] if prof else desc

                # Écriture des données
                writer.writerow([summary, event.get('dtstart').dt, event.get('dtend').dt, desc, prof, location])


ics_to_csv("ADECal.ics", "ADECal.csv")
