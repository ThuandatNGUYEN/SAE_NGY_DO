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
                summary = event.get('summary')
                start_time = event.get('dtstart').dt
                end_time = event.get('dtend').dt
                description = event.get('description')
                location = event.get('location')

                summary = str(summary).replace('\n', ',')
                description = str(description).replace('\n', ',')
                location = str(location).replace('\n', ',')
                desc = description.split(',')
                desc = [item for item in desc if "Exported" not in item and item != ""]
                prof = ""
                if len(desc) > 1:
                    prof = desc[len(desc) - 1]
                # Écriture des données
                writer.writerow([summary, start_time, end_time, desc[:-1], prof, location])



ics_to_csv("ADECal.ics", "ADECal.csv")
