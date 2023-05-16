import Inventory as IN, SavingLoading as SL#, Tutorial as TU

# Lower first for variables and funtions, camelCase
# upper first for filenames and classes, PascalCase
# CONSTANTS
information = SL.InfoToSave()

IN.inventory(100, 2)

def mainMenu():
	userChoice = input("""
	Welcome to The Game!
----------------------------
N - New File
L - Load Existing File
	""") # get user's choice for beginning of game
	if userChoice == 'N':
		print("You chose to open a new file!")
		# create new file, then run game
	elif userChoice == 'L':
		print("You chose to load an existing file!")
		# look for file name, then run it if it exists

# all of the player menus

def intro():
	print("This is the intro text to describe the world to you!")
	# describe the opening as decribed in GameDoc

# inventory menu can go here ---