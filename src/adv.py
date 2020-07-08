from room import Room
from player import Player
import os
# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. 
Dusty passages run north and east."""),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west to north. 
The smell of gold permeates the air."""),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure chamber!
Sadly, it has already been completely emptied by earlier adventurers. 
The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p = Player('outside')
_isPlaying = 1
_nextMove = 1


os.system('cls')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while _isPlaying:
    if (_nextMove):
        print('Current Location: ' + room[p.location].name)
        print(room[p.location].description)
        _nextMove = 0
        to = input('\n*Please Select An Option: N(orth), E(ast), S(outh), W(est) - ')
        if (to == 'n' or to == 'N'):
            if (hasattr(room[p.location], 'n_to')):
                p.location = room[p.location].n_to.key
                ast = '*'*24
                print('\n'+ast+'\n* You have moved North *\n'+ast+'\n')
            else:
                ast = '*'*48
                print('\n'+ast+'\n* You can Not move towards the North from here *\n'+ast+'\n')
        elif (to == 'e' or to == 'E'):
            if (hasattr(room[p.location], 'e_to')):
                p.location = room[p.location].e_to.key
                ast = '*'*23
                print('\n'+ast+'\n* You have moved East *\n'+ast+'\n')
            else:
                ast = '*'*47
                print('\n'+ast+'\n* You can Not move towards the East from here *\n'+ast+'\n')
        elif (to == 's' or to == 'S'):
            if (hasattr(room[p.location], 's_to')):
                p.location = room[p.location].s_to.key
                ast = '*'*24
                print('\n'+ast+'\n* You have moved South *\n'+ast+'\n')
            else:
                ast = '*'*48
                print('\n'+ast+'\n* You can Not move towards the South from here *\n'+ast+'\n')
        elif (to == 'w' or to == 'W'):
            if (hasattr(room[p.location], 'w_to')):
                p.location = room[p.location].w_to.key
                ast = '*'*23
                print('\n'+ast+'\n* You have moved West *\n'+ast+'\n')
            else:
                ast = '*'*47
                print('\n'+ast+'\n* You can Not move towards the West from here *\n'+ast+'\n')
        elif (to == 'q' or to == 'Q'):
            exit()
        else:
            ast = '*'*20
            print('\n'+ast+'\n* Invalid Response *\n'+ast+'\n')
        _nextMove = 1