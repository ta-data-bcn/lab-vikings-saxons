# Soldier

class soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strengh
    
    def receive_damage(self,damage):
        self.health= self.health-damage
    
    
        # Viking
        
class viking(soldier):
    def __init__(self,health,strength,name):
        soldier.__init__(self,health,strength)
        self.name = name
    
   
    def receive_damage(self,damage):
        soldier.receive_damage(self,damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage."
        elif self.health==0:
            return f"{self.name} has died"
        
    def battle_cry():
        print("Odin owns you all")
    
# Saxon

class saxon(soldier):
    def __init__(self,health,strength):
        soldier.__init__(self,health,strength)
        
 
    def receive_damage(self,damage):
        soldier.receive_damage(self,damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died"
           