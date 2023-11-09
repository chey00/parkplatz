def set_parkingspace(row):
    number_plate = input("Bitte geben Sie Ihr Kennzeichen an: ")
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    row[position - 1] = number_plate

parkingspace = [""] * 6

set_parkingspace(parkingspace)
print(parkingspace)
