import csv, subprocess, platform, os

osys = platform.system()
running = True
meny = 0

# def generatePass(length=):

def getFileLocation():
    print('Skriv sökvägen till CSV filen.')
    csvLocation = input("csv: ")
    if os.path.isfile(csvLocation) == False:
        print("Filen existerar inte, vänligen testa igen.")
    elif os.path.isfile(csvLocation) == True:
        print("Filen existerar.")
        global correctCSVLocation
        correctCSVLocation = csvLocation
    else:
        print("gg")

def createADUser():
    



print(f'''Välkommen,
Du kör operativsystemet {osys}.''')

while running:
    if meny == 0:
        try:
            print("\nMeny\nLägg till användare [1]\nRadera användare [2]\nAvsluta [3]")
            meny = int(input("Val: "))
            if  meny == 0 or meny >= 4:
                print("Välj ett av de tillgänliga alternativen.")
                meny = 0
        except:
            print("Välj ett av de tillgänliga alternativen.")
            meny = 0
    if meny == 1:
        getFileLocation()
        meny = 0
        