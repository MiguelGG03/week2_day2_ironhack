
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage

# Viking

class Viking(Soldier):
    
    def __init__(self,name, health, strength):
        super().__init__(health, strength)
        self.name=name

    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if(self.health>0):
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if(self.health>0):
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

# War

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self,viking:Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon:Saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttak(self):
        r=Saxon.receiveDamage(Viking.strength)
        if(Saxon.health>0):
            return  f'{r}'
        else:
            self.saxonArmy.remove(Saxon)

    def saxonAttak(self):
        s=Viking.receiveDamage(Saxon.strength)
        if(Viking.health>0):
            return  f'{s}'
        else:
            self.vikingArmy.remove(Viking)

    def showStatus(self):
        if(len(self.vikingArmy)==0):
            return "Saxons have fought for their lives and survive another day..."
        
        elif(len(self.saxonArmy)==0):
            return f'Vikings have won the war of the century!'

        else:
            return "Vikings and Saxons are still in the thick of battle."
