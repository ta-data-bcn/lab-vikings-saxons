# Soldier
class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receive_damage(self, damage):
        self.health = self.health - damage
        

    
# Viking
class Viking(Soldier):
    
    def __init__(self, health, strength, name):
        Soldier.__init__(self, health, strength)
 #       self.health = health
 #       self.strength = strength
        self.name = name
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return 1
        else:
            return 0
     
    def battle_cry():
        print("Odin Owns You All!")
    

    
# Saxon
class Saxon(Soldier):

    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
#        self.health = health
#        self.strength = strength
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return 1
        else:
            return 0
