# Soldier
class Soldier:
    def __init__(self, health, strength):
        Soldier.health = health
        Soldier.strength = strength
   
    def attack(self):
        return self.strength

    
    def receive_damage(self, damage):
        self.health = self.health - damage
    
# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        self.name = name
        Soldier.__init__(self, health, strength)
    
    def receive_damage(self, damage):
        Soldier.receive_damage(self, damage)
        if self.health > 0:
            #return print(f'{self.name} has received {damage} points of damage')
            return f'{self.name} has received {damage} points of damage'
        else:
            #return print(f'{self.name} had died in combat')
            return f'{self.name} had died in combat'

    def battle_cry():
        return 'Odin Owns You All!'
        
        
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receive_damage(self, damage):
        Soldier.receive_damage(self, damage)
        if self.health > 0:
            #return print(f'A Saxon has received {damage} points of damage')
            return f'A Saxon has received {damage} points of damage'
        else:
            #return print('A Saxon has died in combat')
            return 'A Saxon has died in combat'