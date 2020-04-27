# Soldier
class Soldier:

    # properties or attributes of soldier are health and strength
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    # method attach returns soldier strength
    def attack(self):
        return self.strength
    
    # method receive_damage reduces soldier health attribute
    def receive_damage(self,damage):
        self.health = self.health - damage
        return

# Viking
class Viking(Soldier):
    
    def __init__(self,health,strength,name):
        # super() function: inheritance of attributes and methods
        super().__init__(health,strength)
        # add name attribute
        self.name = name
        
    # method receive_damage tuned for viking
    def receive_damage(self,damage):
        super().receive_damage(damage)
        if self.health > 0:
            print(f"{self.name} has received {damage} points of damage")
        else:
            print(f"{self.name} has died in combat")
        return
    
    # method battle_cry in Vikings class
    def battle_cry(self):
        print("Odin Owns You All!")
    
# Saxon
class Saxon(Soldier):
    
    # method receive_damage tuned for saxon
    def receive_damage(self,damage):
        super().receive_damage(damage)
        if self.health > 0:
            print(f"A Saxon has received {damage} points of damage")
        else:
            print(f"A Saxon has died in combat")
        return
