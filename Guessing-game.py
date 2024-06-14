#guessing game v1.0
import random
import os

def guessing_game():
    zufallszahl = random.randrange(1, 100)
    keintreffer = True
    versuche = 0
    print(f'DEBUG {zufallszahl}')
    while keintreffer:

        Eingabe = input("Gib eine Zahl zwischen 1 und 100 ein:")

        #Prüfen der Eingabe auf Zahl
        """if not Eingabe.isdigit():
            print(f'Fehleingabe durch den Nutzer: {Eingabe} eingegeben.')
            continue"""
        try:
            #Eingabe in Integer umwandeln
            Eingabe = int(Eingabe)
        except:
            print(f'Fehleingabe durch den Nutzer: {Eingabe} eingegeben.')
            continue

        #Prüfen auf Zahl im richtigen Bereich
        if Eingabe < 1 or Eingabe > 100:
            print(f'Fehleingabe durch den Nutzer: {Eingabe} eingegeben.')
            continue

        versuche += 1 #kurzform für: versuche = versuche +1

        #Eingabe auf die Zufallszahl abgleichen
        if Eingabe == zufallszahl:
            keintreffer = False
        if Eingabe > zufallszahl:
            print(f'Gesuchte Zahl ist kleiner')
        if Eingabe < zufallszahl:
            print(f'Gesuchte Zahl ist größer')


    print(f'Die Zahl {Eingabe} ist richtig. Sie haben die Zahl in {versuche} Versuchen erreicht.')
    return versuche

def create_highscore_file(dateiname='werte.txt'):
    if not os.path.exists(dateiname):
        with open(dateiname, 'w') as datei:
            pass
def save_score(versuche, dateiname = 'werte.txt'):
    with open('werte.txt', 'a' ) as highscore:
        highscore.write(f'{versuche}\n')
    print(f'Highscore abgespeichert')

gameloop = True
while gameloop: #Alternativ gameloop durch True ersetzen und die Schleife mit break() abbrechen
    highscore = guessing_game()
    print(f'{highscore}')
    create_highscore_file()
    save_score(highscore)
    newgame = input("Bei erneuten Spiel 'Ja' eingeben, für Beenden Enter drücken:")
    if newgame == "Ja":
        continue
    else:
        gameloop = False