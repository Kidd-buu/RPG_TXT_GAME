# Python Text RPG
# Kidd Buu

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup ####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

#### Title Screen ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() # placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() # placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##############################')
    print('# Welcome to Imagination Land#')
    print('##############################')
    print('          -PLAY-              ')
    print('          -HELP-              ')
    print('          -QUIT-              ')
    print('    Copyright 2023 I.L        ')
    title_screen_selections()

def help_menu():
    print('##############################')
    print('# Welcome to Imagination Land#')
    print('##############################')
    print('-Use up, down, left, right to move')
    print('-Type your commands to do them')
    print('-Use "look" to inspect something')
    print('-Goodluck & Have Fun Adventurer')
    title_screen_selections()

### MAP ###

# Player starts at B2 so they start in area to move around 

#  A1 A2 A3 A4
# -------------
# |  |  |  |  |  A4
#--------------
# |  |  |  |  |  B4
#--------------
# |  |  |  |  |  C4
#--------------
# |  |  |  |  |  D4
# -------------

ZONENAME = ''
DESCRIPTION = "description"
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
    'a1': {
       ZONENAME: 'K-Town',
       DESCRIPTION = 'This is a town'
       EXAMINATION = 'City of Dreams'
       SOLVED = False
       UP = '',
       DOWN = 'b1',
       LEFT = '',
       RIGHT = 'a2',
       
    },
    'b2': {
       ZONENAME: 'HOME',
       DESCRIPTION = 'This is your home!'
       EXAMINATION = 'Place you were born and raised in'
       SOLVED = False
       UP = 'a2',
       DOWN = 'c2',
       LEFT = 'b1',
       RIGHT = 'b3',
       
    },

}

#### WORLD INTERACTIVITY ####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "==========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown Action or Response, Try Again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
        

def player_move(myAction):
    ask = "Where would you like to move to? \n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['south', 'down']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    
def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()

#### Skeleton on how the examine works ####
def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have been here before")
    else:
        print("Trigger event in here")

#### WORLD FUNCTIONALITY ####
def start_game():
    return
