import time
import os
import colorama
import scene
import npc





class Player:
    def __init__(self):
        #Initalize the player starting stats
        self.companions = {}

        self.inventory = {}

        self.achievements = {}

        self.interacted_with = {}

        self.stats = {

            "health": 100,
            "mana": 100,
            "stamina": 100,
            "money": 100

            }

class Game:
    def __init__(self,player):
        self.player = player


