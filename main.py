import time
import os
import colorama
import pickle



#Player Class
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

        self.scenes = {}

    def load_scene(self,scene):
        #Load scene from pre-pickled file of Scene type

        f = open(scene,'rb')

        scene = pickle.load(f)


        #Close out file object
        f.close()


        #add it to scene
        self.scenes[scene.name] = scene

        return True

    def start_game(self):
        print(self.scenes)


