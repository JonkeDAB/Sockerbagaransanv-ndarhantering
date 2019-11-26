import csv, subprocess, platform

osys = platform.system()
running = True
meny = 0

# def generatePass(length=):


print(f'''Välkommen,y
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
        print("Vänligen skriv sökvägen till en csv")
