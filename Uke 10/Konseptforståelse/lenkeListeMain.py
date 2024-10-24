from lenkeListe import Node

def main():
    forste = Node(0)
    siste = forste

    for i in range(1, 10):
        nyNode = Node(i)
        siste.set_neste(nyNode)
        siste = nyNode
    
    peker = forste
    while peker != None:
       print(peker.hent_verdi())
       peker = peker.hent_neste()
    
        
main()