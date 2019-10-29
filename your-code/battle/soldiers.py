# Soldier
class Soldier():
    def __init__(self,health,strength):
        self.health = int(health)
        self.strength = int(strength)
    def attack(self):
        return self.strength 
    def recieve_damage(self,x):
        self.health=self.health - x

# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        Soldier.__init__(self, health, strength)
        self.name = name
    def strength():
        return (int(Soldier.strength))
        
    def recieve_damage(self,x):
        Soldier.recieve_damage(self,x)
        if (int(self.health == 0)): 
           print( self.name , "has died in combat" )
        if (int(self.health >0)):
            print( self.name , "has received" ,x, "of damage" )

    def battle_cry():
        print("Odin owns you all")
    

    
# Saxon
class Saxon(Soldier):
    def __init__ (self,health,strength):
        Soldier.__init__(self,health,strength)
    
    def recieve_damage(self,x):
        Soldier.recieve_damage(self , x)
        if (int(self.health == 0)):
           print( "A Saxon has died in combat" )
        if (int(self.health >0)):
            print( "A Saxon has received ",x," of damage ")
        


new_soldier = Soldier(100,100)


