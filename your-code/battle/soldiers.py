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
    
    def __init__(self,health,strength,name):
        super().__init__(health,strength)
        self.name = name
        
    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health <= 0:
            return f"{self.name} has died in combat"
        else:
            return f"{self.name} has received {damage} points of damage"
    
    
# Saxon
class Saxon(Soldier):
    
    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"
