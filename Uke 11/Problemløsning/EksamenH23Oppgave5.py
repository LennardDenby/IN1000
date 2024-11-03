def stigespill(terningkast: list[int], stiger: dict[int, int]) -> int:
    posisjon = 0
    
    for tall in terningkast:
        posisjon += tall
        if posisjon in stiger:
            posisjon = stiger[posisjon]
    
    return posisjon

def hvilke_tre_kast(slutt_rute: int, stiger: dict[int, int]) -> list[list[int]]:
    mulige_kast = []
    
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                if stigespill([i, j, k], stiger) == slutt_rute:
                    mulige_kast.append([i, j, k])
    
    return mulige_kast
                    

def tester():
    assert stigespill([5,4,2,2],{5:12, 18:7}) == 9
    assert hvilke_tre_kast(5, {3:15, 17:4}) == [[1, 1, 3], [1, 3, 1], [2, 2, 1], [3, 2, 1]]
    
def main():
    tester()

if __name__ == '__main__':
    main()