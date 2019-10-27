# Soldier
class Soldier:
    def __init__(self, health, strength):#, damage):
        self.health = int(health)
        self.strength = int(strength)
        
    def attack(self):
        return self.health
      
    def receive_damage(self, damage):
        self.damage = damage
        self.health = int(self.health - self.damage)
        return self.health


# Viking
class Viking(Soldier):
    #### REMOVE THE BELOW ####
    #damage = 0
    def __init__(self, health, strength, name): #, damage): #4 and 5 are new and only belong to viking
        super().__init__(health, strength)
        self.name = name
        #self.damage = damage

        
#    def receive_damage(self, damage):
#        self.damage = damage
#        self.health = int(self.health - self.damage)
#
#        if int(self.health) > 0:
#            #print(f"{} has received {} points of damage" self.name self.damage)
#            #print(self.name+" has received "+self.damage+" points of damage")
#            return '{} has received {} points of damage'.format(self.name, self.damage)
#        if int(self.health) <= 0:
#            return '{} has died in combat'.format(self.name)                
#                
    def battle_cry(self):
        return "Odin Owns You All!"
        
# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strength): #, damage): #4 and 5 are new and only belong to viking
        super().__init__(health, strength)#, damage)

        
#    def receive_damage(self, damage):
#        self.damage = damage
#        self.health = int(self.health - self.damage)
#        if int(self.health) > 0:
#            return 'A Saxon has received {} points of damage'.format(self.damage)
#        if int(self.health) <= 0:
#            return 'A Saxon has died in combat'.format(self.name)                
                

    
    
    
    