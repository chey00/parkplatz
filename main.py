from datetime import datetime

def set_parkingspace(row, time):
    number_plate = input("Bitte geben Sie Ihr Kennzeichen an: ")
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    if row[position - 1] == "":
        row[position - 1] = number_plate
        time[position - 1] = datetime.now()
    else:
        print("Parkplatz bereits besetzt")

def free_parkingspace(row, time):
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    if row[position - 1] == "":
        print("Parkplatz ist bereits leer")
    else:
        current_time = datetime.now()
        delta = current_time - time[position - 1]

        seconds = delta.total_seconds()
        print("Sie haben", seconds, "Sekunden geparkt.")

        row[position - 1] = ""
        time[position - 1] = None

parkingspace = [""] * 6
parkingtime = [None] * 6

set_parkingspace(parkingspace, parkingtime)
print("Parkplätze", parkingspace)
print("Parkzeit", parkingtime)

free_parkingspace(parkingspace, parkingtime)
print("Parkplätze", parkingspace)
print("Parkzeit", parkingtime)
