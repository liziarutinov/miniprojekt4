"""
Projekt 4: ASCII-ansikten
Ett interaktivt program där användaren kan skapa, klustra och slumpa ASCII-ansikten.
"""

import random
import json


# === FUNKTIONER FÖR ANSIKTEN ===

def skapa_ansikte(ogon, mun, ram):

    return ram[0] + ogon + mun + ogon + ram[1]


def slumpa_ansikte():
   
    ogon_lista = ["o", "-", "^", "x", "T", ">", "@"]
    mun_lista = ["_", "o", "^", "x", "T"]
    ram_lista = ["()", "[]", "{}", "<>", "()]", "[)"]

    ogon = random.choice(ogon_lista)
    mun = random.choice(mun_lista)
    ram = random.choice(ram_lista)

    return skapa_ansikte(ogon, mun, ram)


# === FUNKTIONER FÖR KLUSTER ===

def skriv_ut_kluster(bredd, hojd, ansikte):

    for rad in range(hojd):
        for kolumn in range(bredd):
            print(ansikte, end=" ")
        print()


def skriv_ut_slumpkluster(bredd, hojd):

    for rad in range(hojd):
        for kolumn in range(bredd):
            print(slumpa_ansikte(), end=" ")
        print()


# === MENYFUNKTIONER ===

# Listor för användarval (används i menyval 1)
ogon_alternativ = ["o", "-", "^", "x", "T", ">", "@"]
mun_alternativ = ["_", "o", "^", "x", "T"]
ram_alternativ = ["()", "[]", "{}", "<>", "()]", "[)"]


def skapa_eget_ansikte():

    print("\nVälj ögon:")
    for i, ogon in enumerate(ogon_alternativ, start=1):
        print(f"{i}. {ogon}")

    val_ogon = int(input("Val: ")) - 1

    print("\nVälj mun:")
    for i, mun in enumerate(mun_alternativ, start=1):
        print(f"{i}. {mun}")

    val_mun = int(input("Val: ")) - 1

    print("\nVälj ram:")
    for i, ram in enumerate(ram_alternativ, start=1):
        print(f"{i}. {ram}")

    val_ram = int(input("Val: ")) - 1


    ansikte = skapa_ansikte(
        ogon_alternativ[val_ogon],
        mun_alternativ[val_mun],
        ram_alternativ[val_ram]
    )

    print("\nDitt ansikte:")
    print(ansikte)

    return ansikte
    

def skapa_kluster():

    print("\n1. Skapa eget ansikte")
    print("2. Använd slumpat ansikte")

    val = input("Val: ")

    if val == "1":
        ansikte = skapa_eget_ansikte()
    else:
        ansikte = slumpa_ansikte()
        print(f"Slumpat ansikte: {ansikte}")

    bredd = int(input("Ange bredd: "))
    hojd = int(input("Ange höjd: "))

    skriv_ut_kluster(bredd, hojd, ansikte)


def visa_slump_ansikte():
        print(slumpa_ansikte())


def visa_slumpkluster():

    bredd = int(input("Ange bredd: "))
    hojd = int(input("Ange höjd: "))

    skriv_ut_slumpkluster(bredd, hojd)


# === HUVUDPROGRAM ===

def huvudprogram():
    """Huvudprogrammet som styr menyn och programflödet."""
    while True:
        print("\n--- ASCII-ANSIKTEN ---")
        print("1. Skapa eget ansikte")
        print("2. Skapa kluster (samma ansikte)")
        print("3. Slumpa ett ansikte")
        print("4. Slumpa kluster (blandade ansikten)")
        print("5. Avsluta")
        
        val = input("Välj: ")
        
        if val == "1":
            skapa_eget_ansikte()
        elif val == "2":
            skapa_kluster()
        elif val == "3":
            visa_slump_ansikte()
        elif val == "4":
            visa_slumpkluster()
        elif val == "5":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def farglagg_ansikte(ansikte, farg_kod):

    return farg_kod + ansikte + "\033[0m"


def spara_ansikte_till_json(ansikte, filnamn="sparade_ansikten.json"):

    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            ansikten = json.load(fil)

    except FileNotFoundError:
        ansikten = []

    ansikten.append(ansikte)

    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(ansikten, fil, ensure_ascii=False, indent=4)

    print("Ansikte sparat!")


def ladda_ansikten_fran_json(filnamn="sparade_ansikten.json"):

    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            return json.load(fil)

    except FileNotFoundError:
        return []


# === TURTLE-UTMANING (FÖR DIG MED TURTLE) ===

def rita_ansikte_med_turtle(ogon, mun, ram):

    import turtle

    penna = turtle.Turtle()
    penna.speed(3)

    # Huvud
    penna.penup()
    penna.goto(0, -100)
    penna.pendown()
    penna.circle(100)

    # Vänster öga
    penna.penup()
    penna.goto(-40, 40)
    penna.pendown()
    penna.dot(20)

    # Höger öga
    penna.penup()
    penna.goto(40, 40)
    penna.pendown()
    penna.dot(20)

    # Mun
    penna.penup()
    penna.goto(-40, -20)
    penna.setheading(-60)
    penna.pendown()
    penna.circle(50, 120)

    turtle.done()


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()