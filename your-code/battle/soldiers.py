# Soldier
class Soldier:
    def __init__(self, health, strength):
        Soldier.strength = strength
        Soldier.health = health

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        return self.health - damage


# Viking
class Viking(Soldier):

    def __init__(self, health, strength, name):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in combat"

    def battle_cry(self):
        return print("Odin Owns You All")

    
# Saxon
class Saxon(Soldier):

    def receive_damage(self, damage):
        Soldier.receive_damage(self, damage)
        if Viking.health > 0:
            print(f"A Saxon has received {damage} points of damage")
        elif Viking.health <= 0:
            print("A Saxon has died in combat")
