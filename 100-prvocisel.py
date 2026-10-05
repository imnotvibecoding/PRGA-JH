def je_prvocislo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prvnich_n_prvocisel(pocet):
    prvocisla = []
    cislo = 2
    
    while len(prvocisla) < pocet:
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
        cislo += 1
        
    return prvocisla

if __name__ == "__main__":
    n = 100
    vysledek = prvnich_n_prvocisel(n)
    
    print(f"Prvních {n} prvočísel:")
    print(vysledek)