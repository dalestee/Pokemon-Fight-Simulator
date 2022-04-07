import random
import csv
from fonctions import *
from donnes import *
 
Poke0 = pokemon_data("Charizard")
Poke1 = pokemon_data("Blastoise")
print(Poke0)
print(Poke1)
a = []
print(calc_Stat(int(Poke0[0][6]),100))
print(calc_Stat(int(Poke1[0][7]),100))
for i in range(100):
    a.append(Poke_Attack(Poke0,Poke1,90,"NORMAL","NA"))
print(max(a))
print(min(a))
def max_min(Level, Power, Attack, Defence, Type = 1, Burn = 1, Stab = 1, Item = 1, Passive = 1, Modifiers = 1):
    tab = []
    for i in range(1000):
        tab.append(damage(Level, Power, Attack, Defence, Type, Burn, Stab, Item, Passive, Modifiers))
    return max(tab),min(tab)
print(max_min(100, 90, 204, 236, Type = 1, Burn = 1, Stab = 1, Item = 1, Passive = 1, Modifiers = 1))
