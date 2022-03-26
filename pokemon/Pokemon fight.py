import random
import csv
from damage import damage
from donnes import *
 
def pokemon_data(Nom):  
    with open('pokemon-gen1-data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == Nom:
                return [line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]]        

def Poke_Attack(PA,PD,Attack_Power,Attack_Type,Attack_Tod,Item = 1):
    Type = 1
    if Attack_Type == PA[0][1]:
        Stab = 1.5
    else:
        Stab = 1
        
    if PD[0][0] == 'WATER':
        if Attack_Type in Water_R:
            Type *= 0.5
        elif Attack_Type in Water_W:
            Type *= 2
    if PD[0][0] == 'FIRE':
        if Attack_Type in Fire_R:
            Type *= 0.5
        elif Attack_Type in Fire_W:
            Type *= 2
    if PD[0][0] == 'STEEL':
        if Attack_Type == "POISON":
            Type *= 0
        elif Attack_Type in Steel_R:
            Type *= 0.5
        elif Attack_Type in Steel_W:
            Type *= 2
    if PD[0][0] == 'GRASS':
        if Attack_Type in Grass_R:
            Type *= 0.5
        elif Attack_Type in Grass_W:
            Type *= 2
    if PD[0][0] == 'GHOST':
        if Attack_Type == "FIGHTING" or Attack_Type == "NORMAL":
            Type *= 0
        elif Attack_Type in Ghost_R:
            Type *= 0.5
        elif Attack_Type in Ghost_W:
            Type *= 2
    if PD[0][0] == 'BUG':
        if Attack_Type in Bug_R:
            Type *= 0.5
        elif Attack_Type in Bug_W:
            Type *= 2
    if PD[0][0] == 'NORMAL':
        if Attack_Type == "GHOST":
            Type *= 0 
        elif Attack_Type in Normal_R:
            Type *= 0.5
        elif Attack_Type in Normal_W:
            Type *= 2
    if PD[0][0] == 'POISON':
        if Attack_Type in Poison_R:
            Type *= 0.5
        elif Attack_Type in Poison_W:
            Type *= 2
    if PD[0][0] == 'ELECTRIC':
        if Attack_Type in Electric_R:
            Type *= 0.5
        elif Attack_Type in Electric_W:
            Type *= 2
    if PD[0][0] == 'GROUND':
        if Attack_Type == "ELECTRIC":
            Type *= 0
        elif Attack_Type in Ground_R:
            Type *= 0.5
        elif Attack_Type in Ground_W:
            Type *= 2
    if PD[0][0] == 'FAIRY':
        if Attack_Type == "DRAGON":
            Type *= 0
        elif Attack_Type in Fairy_R:
            Type *= 0.5
        elif Attack_Type in Fairy_W:
            Type *= 2
    if PD[0][0] == 'FIGHTING':
        if Attack_Type in Fighting_R:
            Type *= 0.5
        elif Attack_Type in Fighting_W:
            Type *= 2
    if PD[0][0] == 'PSYCHIC':
        if Attack_Type in Psychic_R:
            Type *= 0.5
        elif Attack_Type in Psychic_W:
            Type *= 2
    if PD[0][0] == 'ROCK':
        if Attack_Type in Rock_R:
            Type *= 0.5
        elif Attack_Type in Rock_W:
            Type *= 2
    if PD[0][0] == 'ICE':
        if Attack_Type in Ice_R:
            Type *= 0.5
        elif Attack_Type in Ice_W:
            Type *= 2
    if PD[0][0] == 'DRAGON':
        if Attack_Type in Dragon_R:
            Type *= 0.5
        elif Attack_Type in Dragon_W:
            Type *= 2
    if PD[0][0] == 'FLYING':
        if Attack_Type == "GROUND":
            Type *= 0
        elif Attack_Type in Flying_R:
            Type *= 0.5
        elif Attack_Type in Flying_W:
            Type *= 2
    if PD[0][0] == 'DARK':
        if Attack_Type == "PSYCHIC":
            Type *= 0
        elif Attack_Type in Dark_R:
            Type *= 0.5
        elif Attack_Type in Dark_W:
            Type *= 2 
    if PD[0][1] == 'none':
        if Attack_Tod == 'SP':
            return damage(100, Attack_Power, int(PA[0][8]), int(PD[0][9]), Stab, Type)
        else:
            return damage(100, Attack_Power, int(PA[0][6]), int(PD[0][7]), Stab, Type)
    else:
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
        if PD[0][0] == 'STEEL':
            if Attack_Type == "POISON":
                Type *= 0
            elif Attack_Type in Steel_R:
                Type *= 0.5
            elif Attack_Type in Steel_W:
                Type *= 2
        if PD[0][1] == 'GRASS':
            if Attack_Type in Grass_R:
                Type *= 0.5
            elif Attack_Type in Grass_W:
                Type *= 2
        if PD[0][0] == 'GHOST':
            if Attack_Type == "FIGHTING" or Attack_Type == "NORMAL":
                Type *= 0
            elif Attack_Type in Ghost_R:
                Type *= 0.5
            elif Attack_Type in Ghost_W:
                Type *= 2
        if PD[0][1] == 'BUG':
            if Attack_Type in Bug_R:
                Type *= 0.5
            elif Attack_Type in Bug_W:
                Type *= 2
        if PD[0][1] == 'NORMAL':
            if Attack_Type == "GHOST":
                Type *= 0
            elif Attack_Type in Normal_R:
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
            if Attack_Type == 'ELECTRIC':
                Type *= 0
            elif Attack_Type in Ground_R:
                Type *= 0.5
            elif Attack_Type in Ground_W:
                Type *= 2
        if PD[0][1] == 'FAIRY':
            if Attack_Type == "DRAGON":
                Type *= 0
            elif Attack_Type in Fairy_R:
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
            if Attack_Type == "GROUND":
                Type *= 0
            elif Attack_Type in Flying_R:
                Type *= 0.5
            elif Attack_Type in Flying_W:
                Type *= 2
        if PD[0][1] == 'DARK':
            if Attack_Type == "PSYCHIC":
                Type *= 0
            elif Attack_Type in Dark_R:
                Type *= 0.5
            elif Attack_Type in Dark_W:
                Type *= 2
    if Attack_Tod == 'SP':
        return damage(100, Attack_Power, int(PA[0][8]), int(PD[0][9]), Stab, Type)
    else:
        return damage(100, Attack_Power, int(PA[0][6]), int(PD[0][7]), Stab, Type)    
Poke0 = pokemon_data("Charizard")
Poke1 = pokemon_data("Blastoise")
print(Poke0)
print(Poke1)
print(Poke_Attack(Poke0,Poke1,80,"NORMAL","SP",Item = 1))
