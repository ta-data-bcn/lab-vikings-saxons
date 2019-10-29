# Soldier
class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receive_damage(self,damage):
        self.health = self.health - damage 

# Viking
class Viking(Soldier):
    def __init__(self,health,strength,name):
        Soldier.__init__(self,health,strength)
        self.name = name
         
    def receive_damage(self,damage):
        Soldier.receive_damage(self,damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage."
        elif self.health <= 0:
            return f"{self.name} has died in combat."
 
    def battle_cry():
        print("Odin Owns You All!") 
    
# Saxon
class Saxon(Soldier):
    def __init__(self,health,strength):
        Soldier.__init__(self,health,strength)
                         
    def receive_damage(self,damage):
        Soldier.receive_damage(self,damage)      
        if self.health > 0:
            return f"A saxon has received {damage} points of damage."
        elif self.health <= 0:
            return "A saxon has died in combat."