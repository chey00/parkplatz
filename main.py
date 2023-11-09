def set_parkingspace(row):
    number_plate = input("Bitte geben Sie Ihr Kennzeichen an: ")
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    if row[position - 1] == "":
        row[position - 1] = number_plate
    else:
        print("Parkplatz bereits besetzt")

def free_parkingspace(row):
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    if position < 1 or position > 6:
        print("Parkplatz exsistiert nicht")
        return

    if row[position - 1] == "":
        print("Parkplatz ist bereits leer")
    else:
        row[position - 1] = ""

parkingspace = [""] * 6

set_parkingspace(parkingspace)
print(parkingspace)

free_parkingspace(parkingspace)
print(parkingspace)
