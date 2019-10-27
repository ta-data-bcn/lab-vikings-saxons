# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.health
        #return '{}'.format(self.health) #its one of these 2
      
    def receive_damage(self, damage):
        self.health = int(self.health - self.damage)


# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name): #4 and 5 are new and only belong to viking
        super().__init__(health, strength)
        self.name = name

    #attack to be inherited from Soldie
        
    def receive_damage(self, damage):
        self.health = self.health - self.damage
        #If the Viking is still alive, the method must return "NAME has received DAMAGE points of damage".
        #If the Viking dies, the method must return "NAME has died in combat".
        if self.health > 0:
            #print(f"{} has received {} points of damage" self.name self.damage)
            #print(self.name+" has received "+self.damage+" points of damage")
            return '{} has received {} points of damage'.format(self.name, self.damage)
        if self.health <= 0:
            return '{} has died in combat'.format(self.name)                
                
    def battle_cry(self):
        return "Odin Owns You All!"
        
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength): #4 and 5 are new and only belong to viking
        super().__init__(health, strength)

    #attack to be inherited from Soldie
        
    def receive_damage(self, damage):
        self.health = self.health - self.damage
        #If the Viking is still alive, the method must return "NAME has received DAMAGE points of damage".
        #If the Viking dies, the method must return "NAME has died in combat".
        if self.health > 0:
            #print(f"{} has received {} points of damage" self.name self.damage)
            #print(self.name+" has received "+self.damage+" points of damage")
            return 'A Saxon has received {} points of damage'.format(self.damage)
        if self.health <= 0:
            return 'A Saxon has died in combat'.format(self.name)                
                

    
    
    
    pass