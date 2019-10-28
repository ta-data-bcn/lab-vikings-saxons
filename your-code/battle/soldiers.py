# Soldier
class Soldier:
    
    def __init__(self, health,strenght):
        self.health = health
        self.strenght = strenght
        
    def attack(self):
        return self.strenght
    
    def receive_damage(self,damage):
        self.health-=damage

# Viking
class Viking(Soldier):
    
    def __init__(self,name,health,strenght):
        Soldier.__init__(self,health,strenght)
        self.name=name
    
        
    def receive_damage(self,damage):
        Soldier.receive_damage(self,damage)
        if self.health>0:
            return (f"{self.name} has received {damage} points of damage.")
        else:
            return (f"{self.name} has died in combat.")

    def battle_cry():
        return "Odin Owns You All!"

    
# Saxon
class Saxon(Soldier):
    def __init__(self,health,strenght):
        Soldier.__init__(self,health,strenght)
    
        
    def receive_damage(self,damage):
        Soldier.receive_damage(self,damage)
        if self.health>0:
            return (f"A Saxon has received {damage} points of damage.")
        else:
            return (f"A Saxon has died in combat.")