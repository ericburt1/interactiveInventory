import Inventory as IN, SavingLoading as SL#, Tutorial as TU

# Lower first for variables and funtions, camelCase
# upper first for filenames and classes, PascalCase
# CONSTANTS
information = SL.InfoToSave()

def mainMenu():
	valid = False  # Valid is just a false variable.
	while not valid: #This will make an infinate loop
		# get user's choice for beginning of game
		userChoice = input("""
    Welcome to The Game!
----------------------------
N - New File
L - Load Existing File
Q - Quit
	""")
		if userChoice != '':
			if userChoice[0].upper() == 'N':
				print("You chose to open a new file!")
				# create new file, then run game
			elif userChoice[0].upper() == 'L':
				print("You chose to load an existing file!")
				# look for file name, then run it if it exists
			elif userChoice[0].upper() == 'Q':
				print("You quit! :(")
				quit()
				#Quits the user
			else:
				print('Invalid Input.')
		else:
			print('Invalid Input.')

# all of the player menus

def intro():
	print("This is the intro text to describe the world to you!")
	# describe the opening as decribed in GameDoc


#IN.inventory(information.inventory, 102, 1) # Remove after testing works.
#IN.printInventory(information.inventory) # Remove after testing works. This should open up menu
IN.inventory(information.inventory,100, 5)
IN.inventory(information.inventory,101, 7)
IN.inventory(information.inventory,102, 2)
IN.inventory(information.inventory,103, 2)
IN.inventory(information.inventory,104, 2)
IN.inventory(information.inventory,105, 2)
IN.printInventory(information.inventory)

mainMenu()

# Varibles can do here
testing = True   #Make this True when testing the game. Make false when not testing game.


# inventory menu can go here ---