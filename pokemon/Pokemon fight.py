import random
import csv
import donnes
def start():
    Pokemon1N = input('Nom pokemon? ')
    Pokemon1Item = input('item? ')
    if Pokemon1Item == '':
        Pokemon1Item = None
    Pokemon2N = input('Nom pokemon adversaire? ')
    Pokemon2Item = input('item? ')
    if Pokemon2Item == '':
        Pokemon2Item = None
    return [pokemon_data(Pokemon1N), Pokemon1Item], [pokemon_data(Pokemon2N), Pokemon2Item]
    
def pokemon_data(Nom):  
    with open('pokemon-gen1-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == Nom:
                return [line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]]    
    
def damage(Level, Power, Attack, Defence, Type = 1, Burn = 1, Stab = 1, Item = 1, Passive = 1, Modifiers = 1):
    if random.randint(1,24) == 25:
        damage = ((((((2*Level)//5) + 2) * Power * Attack/Defence)//50) + 2) * round(random.uniform(0.85,1),2) * Type * Burn * Stab * Item * Passive * Modifiers * 1.5
        return int(damage), ' critical hit!'
    else:
        damage = ((((((2*Level)//5) + 2) * Power * Attack/Defence)//50) + 2) * round(random.uniform(0.85,1),2) * Type * Burn * Stab * Item * Passive * Modifiers

        return int(damage)

def max_min():
    tab = []
    for i in range(1000):
        tab.append(damage(5,40,14,12,1.5))
    return max(tab),min(tab)

def Poke_Attack(PA,PD,Attack_Power,Attack_Type,Attack_Tod,Item):
    Type = 1
    if Attack_Type == PA[0][1]:
        Stab = 1.5
    else:
        Stab = 1
        
    if PD[0][1] == 'WATER':
        if Attack_Type in Water_R:
            Type *= 0.5
        elif Attack_Type in Water_W:
            Type *= 2
    if PD[0][1] == 'FIRE':
        if Attack_Type in Fire_R:
            Type *= 0.5
        elif Attack_Type in Fire_W:
            Type *= 2
    if PD[0][1] == 'STEEL':
        if Attack_Type in Steel_R:
            Type *= 0.5
        elif Attack_Type in Steel_W:
            Type *= 2
    if PD[0][1] == 'GRASS':
        if Attack_Type in Grass_R:
            Type *= 0.5
        elif Attack_Type in Grass_W:
            Type *= 2
    if PD[0][1] == 'GHOST':
        if Attack_Type in Ghost_R:
            Type *= 0.5
        elif Attack_Type in Ghost_W:
            Type *= 2
    if PD[0][1] == 'BUG':
        if Attack_Type in Bug_R:
            Type *= 0.5
        elif Attack_Type in Bug_W:
            Type *= 2
    if PD[0][1] == 'NORMAL':
        if Attack_Type in Normal_R:
            Type *= 0.5
        elif Attack_Type in Normal_W:
            Type *= 2
    if PD[0][1] == 'POISON':
        if Attack_Type in Poison_R:
            Type *= 0.5
        elif Attack_Type in Poison_W:
            Type *= 2
    if PD[0][1] == 'ELECTRIC':
        if Attack_Type in Electric_R:
            Type *= 0.5
        elif Attack_Type in Electric_W:
            Type *= 2
    if PD[0][1] == 'GROUND':
        if Attack_Type in Ground_R:
            Type *= 0.5
        elif Attack_Type in Ground_W:
            Type *= 2
    if PD[0][1] == 'FAIRY':
        if Attack_Type in Fairy_R:
            Type *= 0.5
        elif Attack_Type in Fairy_W:
            Type *= 2
    if PD[0][1] == 'FIGHTING':
        if Attack_Type in Fighting_R:
            Type *= 0.5
        elif Attack_Type in Fighting_W:
            Type *= 2
    if PD[0][1] == 'PSYCHIC':
        if Attack_Type in Psychic_R:
            Type *= 0.5
        elif Attack_Type in Psychic_W:
            Type *= 2
    if PD[0][1] == 'ROCK':
        if Attack_Type in Rock_R:
            Type *= 0.5
        elif Attack_Type in Rock_W:
            Type *= 2
    if PD[0][1] == 'ICE':
        if Attack_Type in Ice_R:
            Type *= 0.5
        elif Attack_Type in Ice_W:
            Type *= 2
    if PD[0][1] == 'DRAGON':
        if Attack_Type in Dragon_R:
            Type *= 0.5
        elif Attack_Type in Dragon_W:
            Type *= 2
    if PD[0][1] == 'FLYING':
        if Attack_Type in Flying_R:
            Type *= 0.5
        elif Attack_Type in Flying_W:
            Type *= 2
    if PD[0][1] == 'DARK':
        if Attack_Type in Dark_R:
            Type *= 0.5
        elif Attack_Type in Dark_W:
            Type *= 2
            
    if PD[0][2] == 'none':
        if Attack_Tod == 'SP':
            return damage(100, Power, PA[0][8], PD[1][9], Stab, Type)
        else:
            return damage(100, Power, PA[0][6], PD[1][7], Stab, Type)
    else:
        if PD[0][2] == 'WATER':
            if Attack_Type in Water_R:
                Type *= 0.5
            elif Attack_Type in Water_W:
                Type *= 2
    if PD[0][2] == 'FIRE':
        if Attack_Type in Fire_R:
            Type *= 0.5
        elif Attack_Type in Fire_W:
            Type *= 2
    if PD[0][2] == 'STEEL':
        if Attack_Type in Steel_R:
            Type *= 0.5
        elif Attack_Type in Steel_W:
            Type *= 2
    if PD[0][2] == 'GRASS':
        if Attack_Type in Grass_R:
            Type *= 0.5
        elif Attack_Type in Grass_W:
            Type *= 2
    if PD[0][2] == 'GHOST':
        if Attack_Type in Ghost_R:
            Type *= 0.5
        elif Attack_Type in Ghost_W:
            Type *= 2
    if PD[0][2] == 'BUG':
        if Attack_Type in Bug_R:
            Type *= 0.5
        elif Attack_Type in Bug_W:
            Type *= 2
    if PD[0][2] == 'NORMAL':
        if Attack_Type in Normal_R:
            Type *= 0.5
        elif Attack_Type in Normal_W:
            Type *= 2
    if PD[0][2] == 'POISON':
        if Attack_Type in Poison_R:
            Type *= 0.5
        elif Attack_Type in Poison_W:
            Type *= 2
    if PD[0][2] == 'ELECTRIC':
        if Attack_Type in Electric_R:
            Type *= 0.5
        elif Attack_Type in Electric_W:
            Type *= 2
    if PD[0][2] == 'GROUND':
        if Attack_Type in Ground_R:
            Type *= 0.5
        elif Attack_Type in Ground_W:
            Type *= 2
    if PD[0][2] == 'FAIRY':
        if Attack_Type in Fairy_R:
            Type *= 0.5
        elif Attack_Type in Fairy_W:
            Type *= 2
    if PD[0][2] == 'FIGHTING':
        if Attack_Type in Fighting_R:
            Type *= 0.5
        elif Attack_Type in Fighting_W:
            Type *= 2
    if PD[0][2] == 'PSYCHIC':
        if Attack_Type in Psychic_R:
            Type *= 0.5
        elif Attack_Type in Psychic_W:
            Type *= 2
    if PD[0][2] == 'ROCK':
        if Attack_Type in Rock_R:
            Type *= 0.5
        elif Attack_Type in Rock_W:
            Type *= 2
    if PD[0][2] == 'ICE':
        if Attack_Type in Ice_R:
            Type *= 0.5
        elif Attack_Type in Ice_W:
            Type *= 2
    if PD[0][2] == 'DRAGON':
        if Attack_Type in Dragon_R:
            Type *= 0.5
        elif Attack_Type in Dragon_W:
            Type *= 2
    if PD[0][2] == 'FLYING':
        if Attack_Type in Flying_R:
            Type *= 0.5
        elif Attack_Type in Flying_W:
            Type *= 2
    if PD[0][2] == 'DARK':
        if Attack_Type in Dark_R:
            Type *= 0.5
        elif Attack_Type in Dark_W:
            Type *= 2
    if Attack_Tod == 'SP':
        return damage(100, Power, PA[0][8], PD[1][9], Stab, Type)
    else:
        return damage(100, Power, PA[0][6], PD[1][7], Stab, Type)    
Poke = start()
Poke0 = Poke[0]
Poke1 = Poke[1]