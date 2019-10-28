# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.health
      
#    def receive_damage(self, damage):
#        self.damage = damage
#        self.health = self.health -= self.damage
#        return self.health


# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
        
    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if int(self.health) > 0:
           #print(f"{} has received {} points of damage", self.name, self.damage)
            #print(self.name+" has received "+self.damage+" points of damage")
            print('{} has received {} points of damage'.format(self.name, self.damage))
        else:
            return '{} has died in combat'.format(self.name)                
                
    def battle_cry(self):
        return "Odin Owns You All!"
        
# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

        
    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if int(self.health) > 0:
            #return 
            print('A Saxon has received {} points of damage'.format(self.damage))
        else:
        #if int(self.health) <= 0:
            return print(f'A Saxon has died in combat')
                

    
    
    
    