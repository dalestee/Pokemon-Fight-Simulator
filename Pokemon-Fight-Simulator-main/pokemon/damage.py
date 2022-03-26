import random
def damage(Level, Power, Attack, Defence, Type = 1, Burn = 1, Stab = 1, Item = 1, Passive = 1, Modifiers = 1):
    if random.randint(1,24) == 24:
        damage = ((((((2*Level)//5) + 2) * Power * Attack/Defence)//50) + 2) * round(random.uniform(0.85,1),2) * Type * Burn * Stab * Item * Passive * Modifiers * 1.5
        return int(damage)
    else:
        damage = ((((((2*Level)//5) + 2) * Power * Attack/Defence)//50) + 2) * round(random.uniform(0.85,1),2) * Type * Burn * Stab * Item * Passive * Modifiers

        return int(damage)

def max_min(Level, Power, Attack, Defence, Type = 1, Burn = 1, Stab = 1, Item = 1, Passive = 1, Modifiers = 1):
    tab = []
    for i in range(1000):
        tab.append(damage(Level, Power, Attack, Defence, Type, Burn, Stab, Item, Passive, Modifiers))
    return max(tab),min(tab)
