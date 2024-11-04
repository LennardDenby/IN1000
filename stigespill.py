def stigespill(terningkast: list[int], stiger: dict[int, int]) -> int:
    posisjon = 0
    
    for tall in terningkast:
        posisjon += tall
        
        if posisjon in stiger:
            posisjon = stiger[posisjon]
    
    return posisjon

def hvilke_tre_kast(slutt_rute: int, stiger: dict[int, int]) -> list[list[int]]:
    returListe = []
    
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if stigespill([i, j, k], stiger) == slutt_rute:
                    returListe.append([i, j, k])
    
    return returListe

def main():
    print(hvilke_tre_kast(5, {3:15, 17:4}) )

if __name__ == '__main__':
    main()