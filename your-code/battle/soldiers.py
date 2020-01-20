# Soldier
class Soldier:
    def __Init__(self, strenght, health):
        self.strenght = strenght
        self.health = health
        
    def attack(self):
        return self.strenght
    
    def receive_damage(self, damage):
        return health = health - damage
        
    
# Viking
class Viking(Soldier):
    
    def __Init__(self, strenght, health, name):
        super().__init__(strenght, health) 
        self.name = name
    
    
    def attack(self): 
        return self.strenght
    
    def receive_damage(self, damage, name):
        health = health - damage
        if health > 0:
            print(self.name, "has received", self.damage, "points of damage")
        else:
            print(self.name, "has died in combat")
        
    def battle_cry(self):
        print ("Odin Owns You All!")
    
    
# Saxon
class Saxon(Soldier):
    
     def __Init__(self, strenght, health):
        super().__init__(strenght, health)
        self.name = name
    
    def attack(self): 
        return self.strenght
    
    def receive_damage(self, damage):
        health = health - damage
        if health > 0:
            print("A Saxon has received", self.damage, "points of damage")
        else:
            print("A Saxon has died in combat")
        
        