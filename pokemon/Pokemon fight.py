import random
import csv
from fonctions import *
from donnes import *
 
Poke0 = pokemon_data("Charizard")
Poke1 = pokemon_data("Blastoise")
print(Poke0)
print(Poke1)
a = []
Attack_Power = calc_Stat(int(Poke0[0][6]),100,Nature = 1,IV = 0,EV = 0)
for i in range(100):
    a.append(Poke_Attack(Poke0,Poke1,90,"NORMAL","NA"))
print(max(a))
print(min(a))
    
