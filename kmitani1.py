import math
import time

znak = "O"        # zkus "*" nebo "●" — když spadne UnicodeEncodeError, terminál neumí unicode, vrať "O"
amplituda = 30      # jak daleko se kulička vychýlí (počet znaků)
rychlost = 0.25     # jak rychle kmitá (větší číslo = rychleji)

for krok in range(150):
    cas = krok * rychlost
    vychylka = math.sin(cas)                    # číslo mezi -1 a 1
    pozice = int(amplituda + amplituda * vychylka)
    print(" " * pozice + znak)
    time.sleep(0.04)
