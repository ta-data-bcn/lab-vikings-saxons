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
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            print('{} has received {} points of damage'.format(self.name, damage))
        else:
            print('{} has died in combat'.format(self.name))
    def battle_cry():
        print('Odin Owns You All!!')
# Saxon
class Saxon(Soldier):
     def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            print('A saxon has received {} points of damage'.format(damage))
        else:
            print('A saxon has died in combat')