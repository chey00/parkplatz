def set_parkingspace(row):
    number_plate = input("Bitte geben Sie Ihr Kennzeichen an: ")
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    row[position - 1] = number_plate

def free_parkingspace(row):
    position = int(input("Bitte geben Sie die Parkplatznummer an: "))

    row[position - 1] = ""

parkingspace = [""] * 6

set_parkingspace(parkingspace)
print(parkingspace)

free_parkingspace(parkingspace)
print(parkingspace)
