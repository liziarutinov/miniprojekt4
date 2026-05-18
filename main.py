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
    """
    Skriver ut ett kluster (rutnät) av samma ansikte.
    
    Parametrar:
        bredd (int): Antal ansikten per rad
        hojd (int): Antal rader
        ansikte (str): Ansiktet som ska upprepas
    """
    # TODO: Implementera funktionen
    # Tips: Använd nästlade loopar (for rad in range(hojd): for kolumn in range(bredd))
    # Tips: print(ansikte, end=" ") för att skriva ut på samma rad
    # Tips: print() efter innerloopen för att byta rad
    pass


def skriv_ut_slumpkluster(bredd, hojd):
    """
    Skriver ut ett kluster (rutnät) med slumpade ansikten.
    
    Parametrar:
        bredd (int): Antal ansikten per rad
        hojd (int): Antal rader
    """
    # TODO: Implementera funktionen
    # Tips: Använd nästlade loopar
    # Tips: Anropa slumpa_ansikte() för varje position
    pass


# === MENYFUNKTIONER ===

# Listor för användarval (används i menyval 1)
ogon_alternativ = ["o", "-", "^", "x", "T", ">", "@"]
mun_alternativ = ["_", "o", "^", "x", "T"]
ram_alternativ = ["()", "[]", "{}", "<>", "()]", "[)"]


def skapa_eget_ansikte():
    """
    Låter användaren designa ett eget ansikte genom menyval.
    Skriver ut resultatet.
    """
    # TODO: Implementera funktionen
    # 1. Visa meny för ögon (nummer + tecken)
    # 2. Fråga efter val (1-7)
    # 3. Gör samma för mun (1-5)
    # 4. Gör samma för ram (1-6)
    # 5. Anropa skapa_ansikte() och skriv ut resultatet
    pass


def skapa_kluster():
    """
    Låter användaren skapa ett kluster med samma ansikte.
    Först väljer eller skapar användaren ett ansikte.
    """
    # TODO: Implementera funktionen
    # 1. Fråga: Vill du använda ett befintligt ansikte eller skapa nytt?
    # 2. Om nytt: anropa skapa_eget_ansikte() eller skapa_ansikte() direkt
    # 3. Fråga efter bredd och höjd
    # 4. Anropa skriv_ut_kluster()
    pass


def visa_slump_ansikte():
    """Visar ett slumpmässigt ansikte."""
    # TODO: Anropa slumpa_ansikte() och skriv ut resultatet
    pass


def visa_slumpkluster():
    """
    Låter användaren skapa ett kluster med slumpade ansikten.
    Frågar efter bredd och höjd.
    """
    # TODO: Fråga efter bredd och höjd
    # TODO: Anropa skriv_ut_slumpkluster()
    pass


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
    """
    Lägger till ANSI-färgkoder runt ett ansikte.
    
    Parametrar:
        ansikte (str): Ansiktet som ska färgläggas
        farg_kod (str): ANSI-färgkod (t.ex. "\033[91m")
    
    Returnerar:
        str: Ansikte med färgkoder
    """
    # TODO: return farg_kod + ansikte + "\033[0m"
    pass


def spara_ansikte_till_json(ansikte, filnamn="sparade_ansikten.json"):
    """Sparar ett ansikte till en JSON-fil."""
    # TODO: Importera json
    # TODO: Ladda befintlig lista, lägg till nytt ansikte, spara
    pass


def ladda_ansikten_fran_json(filnamn="sparade_ansikten.json"):
    """Laddar sparade ansikten från en JSON-fil."""
    # TODO: Använd json.load() och returnera listan
    pass


# === TURTLE-UTMANING (FÖR DIG MED TURTLE) ===

def rita_ansikte_med_turtle(ogon, mun, ram):
    """
    EXTRA UTMANING: Ritar ett ansikte med Turtle-grafik istället för ASCII.
    Detta är för de som har tillgång till Turtle-biblioteket.
    """
    # TODO: Importera turtle
    # TODO: Skapa en turtle
    # TODO: Rita två cirklar som ögon
    # TODO: Rita en båge som mun
    # TODO: Rita en cirkel som huvud (ram)
    # TODO: turtle.done()
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()