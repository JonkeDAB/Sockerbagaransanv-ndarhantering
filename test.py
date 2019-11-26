import os

def getFileLocation():
    print('Skriv sökvägen till CSV filen.')
    csvlocation = input("csv: ")
    if os.path.isfile(csvlocation) == False:
        print("Filen existerar inte, vänligen testa igen.")
    elif os.path.isfile(csvlocation) == True:
        print("Filen existerar.")
        correctcsvlocation = csvlocation
    else:
        print("gg")
        
    return correctcsvlocation

print(getFileLocation())