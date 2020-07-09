from room import Room
from player import Player
from item import Item
import os
import time

# Declare items
items = {
    1: Item(1, 'Chest Key', 'I can use this to unlock something, but what?'),
    2: Item(2, 'Steel Sword', 'This will come in handy'),
    3: Item(3, 'Torch', 'It\'s not very bright, but it helps'),
    4: Item(4, 'Ruby', 'I\'m Rich!'),
    5: Item(5, 'Rope', 'The best thing since spliced string'),
    6: Item(6, 'Tattered Journal', 'I can\'t make out what these markings are'),
    7: Item(7, 'Strange Orb', 'Shiny!')
}

# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items[3]]),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. 
Dusty passages run north and east.""", [items[2]]),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [items[7], items[6]]),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west to north. 
The smell of gold permeates the air.""", [items[1], items[5]]),

    'treasure': Room('treasure', "Treasure Chamber", "You've found the long-lost treasure chamber!", [items[4]]),
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

p = Player('outside', [])
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
        cmd = input('\n What would you like to do? S(earch), I(nventory), M(ove), Q(uit) - ')
        if (cmd == 'm' or cmd == 'M'):
            cmd = input('\n*Please Select An Option: N(orth), E(ast), S(outh), W(est) - ')
            if (cmd == 'n' or cmd == 'N'):
                if (hasattr(room[p.location], 'n_to')):
                    p.location = room[p.location].n_to.id
                    ast = '*'*24
                    print('\n'+ast+'\n* You have moved North *\n'+ast+'\n')
                else:
                    ast = '*'*48
                    print('\n'+ast+'\n* You can Not move towards the North from here *\n'+ast+'\n')
            elif (cmd == 'e' or cmd == 'E'):
                if (hasattr(room[p.location], 'e_to')):
                    p.location = room[p.location].e_to.id
                    ast = '*'*23
                    print('\n'+ast+'\n* You have moved East *\n'+ast+'\n')
                else:
                    ast = '*'*47
                    print('\n'+ast+'\n* You can Not move towards the East from here *\n'+ast+'\n')
            elif (cmd == 's' or cmd == 'S'):
                if (hasattr(room[p.location], 's_to')):
                    p.location = room[p.location].s_to.id
                    ast = '*'*24
                    print('\n'+ast+'\n* You have moved South *\n'+ast+'\n')
                else:
                    ast = '*'*48
                    print('\n'+ast+'\n* You can Not move towards the South from here *\n'+ast+'\n')
            elif (cmd == 'w' or cmd == 'W'):
                if (hasattr(room[p.location], 'w_to')):
                    p.location = room[p.location].w_to.id
                    ast = '*'*23
                    print('\n'+ast+'\n* You have moved West *\n'+ast+'\n')
                else:
                    ast = '*'*47
                    print('\n'+ast+'\n* You can Not move towards the West from here *\n'+ast+'\n')
        elif (cmd == 'q' or cmd == 'Q'):
            os.system('cls')
            exit()
        elif (cmd == 'i' or cmd == 'I'):
            if (len(p.items) == 0):
                print('***\n*Backpack\n')
                print('Empty\n')
                print('*\n***\n')
            else:
                print('***\n*Backpack\n')
                for i in p.items:
                    print('* '+str(i.id)+') '+i.name+': '+i.description+'\n')
                print('*\n***\n')
                cmd = input('You can drop an item by selecting it\'s id, or enter nothing to continue - ')
                if (len(cmd) > 0):
                    for i in p.items:
                        if (str(i.id) == cmd):
                            room[p.location].items.append(items[int(cmd)])
                            p.items.remove(i)
                            print('You drop the item to the floor')
                    print('\n')
                elif (cmd == ''):
                    print('You close your backpack, and venture on\n')
                else:
                    print('Invalid Option\n')
        elif (cmd == 's' or cmd == 'S'):
            print('You search the room...')
            time.sleep(1)
            print('...\n')
            time.sleep(1)
            if (p.location == 'treasure'):
                x = 0
                for i in p.items:
                    if (i.id == 1):
                        x = 1
                if (x == 1):
                    print('You use your key on the chest')
                    time.sleep(1)
                    print('It fits!')
                    time.sleep(2)
                    print('You slowly open the chest, as a dim red glow shines out')
                    time.sleep(2)
                    if (len(room[p.location].items) > 0):
                        for i in room[p.location].items:
                            p.items.append(items[i.id])
                            room[p.location].items.clear()
                        print('You find a giant ruby inside!\n')
                    else:
                        print('It appears you have already taken the ruby\n')
                else:
                    print('You see a chest in the center of the room, but you do not have a way of opening it')
            elif (len(room[p.location].items) > 0):
                for i in room[p.location].items:
                    p.items.append(items[i.id])
                room[p.location].items.clear()
                print('You find some items!\n')
            else:
                print('Sadly, the room contains nothing useful\n')
        else:
            ast = '*'*20
            print('\n'+ast+'\n* Invalid Response *\n'+ast+'\n')
        _nextMove = 1