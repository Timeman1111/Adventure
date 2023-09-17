import time
import os
import colorama
import pickle
from game_functions import *

clear()


#Player Class
class Player:
    def __init__(self):
        #Initalize the player starting stats

        self.name = None

        self.tutorial = True

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


    def request_name(self):
        while True:
            user = input("NAME: ")

            try: 
                int(user)
                scrollTxt('\nTry Again!')
                continue
            except:
                self.player.name = user

                return


    def tutorial(self):

        scrollTxt('Hello\n\n',0.045)

        scrollTxt('This is a quick tutorial on how to play the game!\n\n',delay = 0.045)

        scrollTxt('What is your name?',delay = 0.045)

        self.request_name()

        scrollTxt(f'Thanks {self.player.name}')


    def start_game(self):

        if self.player.tutorial == True:

            self.tutorial()


game = Game(Player())

game.start_game()
