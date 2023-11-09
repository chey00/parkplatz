from datetime import datetime

# Die Funktion verwaltet Parkplätze, welche über den Parameter row manipuliert werden.
# Der Parameter time wird erst für die Aufgabe 5 benötigt.
def set_parkingspace(row, time):
    # Der Benutzer gibt sein Kennzeichen sowie die Parkplatznummer ein. Die Parkplatznummer wird in eine Ganzahl
    # umgewandelt.
    number_plate = input("Bitte geben Sie Ihr Kennzeichen an: ")
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    # Prüft, ob die Parkplatznummer in einem gültigen Bereich liegt.
    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    # Prüft eine mögliche Doppelbelegung des Parkplatzes
    if row[position - 1] == "":
        # Falls der Parkplatz noch nicht belegt ist, wird das Kennzeichen gespeichert.
        row[position - 1] = number_plate
        time[position - 1] = datetime.now()
    else:
        # Andernfalls erscheint für den Benutzer eine Fehlermeldung.
        print("Parkplatz bereits besetzt")

# Diese Funktion simuliert das Verlassen eines Parkplatzes.
# Der Parameter time wird erst für die Aufgabe 5 benötigt.
def free_parkingspace(row, time):
    # Die Parkplatznummer wird über eine Benutzereingabe ermittelt. Anhand der Parkplatznummer wird später das
    # Kennzeichen gelöscht. Die Eingabe wird zu einer Ganzzahl umgewandelt.
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    # Prüft, ob die Parkplatznummer in einem gültigen Bereich liegt.
    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    # Prüfung, ob ein Parkplatz wirklich belegt ist.
    if row[position - 1] == "":
        # In diesen Fall war der Parkplatz nicht belegt
        print("Parkplatz ist bereits leer")
    else:
        # Wird erst für Aufgabe 5 benötigt.
        current_time = datetime.now()
        delta = current_time - time[position - 1]


        seconds = delta.total_seconds()
        print("Sie haben", seconds, "Sekunden geparkt.")

        # Der Parkplatz war belegt und wird nun als frei gekennzeichnet.
        row[position - 1] = ""
        time[position - 1] = None

# Die Variablen zur Speicherung der Kennzeichen und Parkdauer werden für sechs Parkplätze erstellt.
parkingspace = [""] * 6
parkingtime = [None] * 6

# Simulation des Einparken auf dem Parkplatz.
# Der Funktion werden die oberen Variablen mitgegeben, damit Änderungen gespeichert werden können
set_parkingspace(parkingspace, parkingtime)
print("Parkplätze", parkingspace)
print("Parkzeit", parkingtime)

# Simulation des Ausparkens auf dem Parkplatz.
free_parkingspace(parkingspace, parkingtime)
print("Parkplätze", parkingspace)
print("Parkzeit", parkingtime)
