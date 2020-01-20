# Soldier
class Soldier:
    def __init__(self, strenght, health):
        self.strenght = strenght
        self.health = health
        
    def attack(self):
        return self.strenght
    
    def receive_damage(self, damage):
        self.health -= damage
        
    
# Viking
class Viking(Soldier):
    
    def __init__(self, strenght, health, name):
        super().__init__(strenght, health) 
        self.name = name
     
    def receive_damage(self, damage):
        self.health -= damage
        if health > 0:
            print(self.name, "has received", damage, "points of damage")
        else:
            print(self.name, "has died in combat")
        
    def battle_cry():
        print ("Odin Owns You All!")
    
    
# Saxon
class Saxon(Soldier):
    
    def receive_damage(self, damage):
        self.health -= damage
        if health > 0:
            print("A Saxon has received", damage, "points of damage")
        else:
            print("A Saxon has died in combat")
        
        