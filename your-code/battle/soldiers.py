# Soldier
class Soldier:
    def __init__(self, health, strength): #
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength
#methods are functions. with methods you need paranthesis. with attribute you dont need them.
    
    def receive_damage(self, damage):
        self.health=self.health-damage
#damage is not an attribute of the class. it will be passed as an attrbitue for this method. so we dont have to do self.damage
  

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health,strength)
        self.name=name
    
    def receive_damage(self, damage):
        Soldier.receive_damage(self,damage)
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        elif health<=0:
            return f"{self.name} has died in combat"
        
    def battle_cry():
        print("Odin Owns You All!")
 
#if we write again another attack method in Vikings or Saxon, we overwrite the one in Soldier class. So it will ignore the soldier one and use the new one. 
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health,strength)
  
    def receive_damage(self,damage):
        Soldier.receive_damage(self,damage)
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health<=0:
            return f"A Saxon has died in combat"