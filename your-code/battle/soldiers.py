# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack():
        return strength
    
    def receive_damage(damage):
        return health - damage

# Viking
class Viking(Soldier):
    def __init__(self, name):
        self.name = name

    def battle_cry():
        return print("Odin Owns You All!")

    def receive_damage(damage):
        health - damage
        if Viking.health > 0:
            return print("{name} has received {damage} points of damage")
        else:
            return print('{name} has died in combat!')
    
# Saxon
class Saxon(Soldier):
    pass