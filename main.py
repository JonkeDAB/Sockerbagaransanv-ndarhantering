import csv, subprocess, platform, os

osys = platform.system()
running = True
meny = 0

# def generatePass(length=):

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




print(f'''Välkommen,
Du kör operativsystemet {osys}.''')

while running:
    if meny == 0:
        try:
            print("\nMeny\nLägg till användare [1]\nRadera användare [2]\nAvsluta [3]")
            meny = input("Val: ")
            if meny == 0 or meny >= 4:
                print("Välj ett av de tillgänliga alternativen.")
                meny = 0
        except:
            print("Välj ett av de tillgänliga alternativen.")
            meny = 0
    if meny == 1: