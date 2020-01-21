#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        return self.health - damage

#Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died proudly in the combat. He went to the Valhalla")
        
    def battle_cry():
        return "Odin Owns You All !"

#Saxon
class Saxon(Soldier):

    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died proudly in combat")