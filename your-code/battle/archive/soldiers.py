# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.health
      
    def receive_damage(self, damage):
        self.health -= self.damage


# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
        
    def receive_damage(self, damage):
        Solider.receive_damage(self, damage)
        if int(self.health) > 0:
            print('{} has received {} points of damage'.format(self.name, self.damage))
        else:
            return '{} has died in combat'.format(self.name)                
                
    def battle_cry(self):
        return "Odin Owns You All!"
        
# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receive_damage(self, damage):
        Solider.receive_damage(self, damage)
        if int(self.health) > 0:
            print('A Saxon has received {} points of damage'.format(self.damage))
        else:
            return print(f'A Saxon has died in combat')
                

    
    
    
    