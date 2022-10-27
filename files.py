from vikingsClasses import *
from vikingsClasses import (Viking,Saxon,War,Soldier)

def main():
    saxon=Saxon(100,98)
    viking=Viking('Lewandoski',100,99)
    guerra=War()

    guerra.addSaxon(saxon)
    guerra.addViking(viking)
    ataque1=guerra.saxonAttack()
    ataque2=guerra.vikingAttack()
    estadisticas=guerra.showStatus()
    lista1=guerra.saxonArmy
    lista2=guerra.vikingArmy
    print(f'Ataque Saxon: {ataque1}\n'
          f'Ataque Viking: {ataque2}\n'
          f'Estadisticas: {estadisticas}\n'
          f'Ejercito Saxon: {lista1}\n'
          f'Ejercito Viking: {lista2}\n')
    #vuelvo a atacar para que uera un vikingo
    ataque3=guerra.saxonAttack()
    estadisticas2=guerra.showStatus()
    print(f'Ataque Saxon: {ataque3}\n'
          f'Estadisticas: {estadisticas2}\n'
          f'Ejercito Saxon: {lista1}\n'
          f'Ejercito Viking: {lista2}\n')







if __name__=='__main__':
    main()