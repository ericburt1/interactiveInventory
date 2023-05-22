
#If you create a new item make sure to add a description for it in the same spot in the description dictionary
itemID_dictionary = {100: "Dirt", 
					101: "Brick", 
					102: "Wood", 
					103: "Computer Monitor", 
					104: "Metal Shards", 
					105: "Spear tips"}
# The items should be in line with each other in both dictionares
# Item descriptions could be more detailed. Depends if it owuld fit into the game.
itemDescription_dictionary = {"Dirt": 'A handful of dirt.',
							 "Brick": 'Used in some buildings. Seems to be made of clay.', 
							 "Wood": 'A log of wood.', 
							 "Computer Monitor": "This foreign object is new to you. You don't fully know what it is.", 
							 "Metal Shards": "This could be used for many things. Maybe you could melt this down.", 
							 "Spear tips": "You could put this on the end of a spear. It seems sharp.",
							 }

def inventory(inventory, itemID, amount):
	from Menus import information as M#, testing as test   # This is just importing the class information
	sections = 0   # This is used to get the section area
	notIn = 0   # This is a var to count if its not in
	if len(inventory) < (M.bagSize*5):
		for slot in range(0, len(inventory)):
			if itemID == inventory[sections][0]:
				M.inventory[sections][1] = amount   # This sets the section with the correct ID next slot to the correct amount
				#if test == True:
				#	print(inventory[sections])   # Prints if testing is true
				break
			else:
				notIn += 1   # This will add 1 to not in if the one being checked is not the correct ID
			sections += 1   # This adds one to the section it will look at
		if notIn == len(inventory):
			newItem = [itemID, amount]   # This creates a array to store the itemID, and amount
			M.inventory.append(newItem)   # This will add the newItem which is the array to the inventory
			#print(M.inventory)   # prints Inventory
	elif len(inventory) == (M.bagSize*5):
		print('Your inventory is full.')
	else:
		print('Your inventory should not be this size.')
	#print(len(M.inventory))

def printInventory(inventory):
	from Menus import information as M
	sections = 0
	sections2 = 0
#	for slot in range(0,len(inventory)):
#		part = inventory[sections][0]
#		print(f"SLOT {sections}: You have {inventory[sections][1]} pieces of {itemID_dictionary[part]}.")
#		sections += 1 
# Un comment above section if you want it to display the inventory when the load up printInventory
	valid = False
	while not valid:
		#Gets use choice
		userChoice = input(f'''
    Inventory
   Bag Size: {M.bagSize*5}
  Total Items: {len(inventory)}
------------------
L - Look at item
D - Display inventory
Q - Quit

''')
		if userChoice != '': # Makes sure the user doesn't just press enter
			if userChoice[0].upper() == 'L': # This gets the first letter and capitalizes it to check
				valid2 = False
				while not valid2:
					userChoice3 = 0 # Sests user choice in this while
					valid3 = False
					while not valid3:
						try: #Trying to make sure userchoice3 is a int
							userChoice3 = int(input('\nWhat item do you want to look at?\n')) # Asks user for their input
							if userChoice3 in range(0,50): # if the user choice in 0-50
								break
							elif userChoice3 > 50: # If the user input greater than 5 
								print('\nThat number is to large.\n')
							elif userChoice3 < 0:  # if the user input less than 0
								print('\nThat number is to small.\n')
							else: # otherwise
								print('\nMust be a number!\n')
						except ValueError: # If userChoice3 not a int this will play
							print('That does not work.')
					if userChoice3 in range(0, len(inventory)): # if userchoice3 in the range of the inventory
						spot = itemID_dictionary[inventory[userChoice3][0]] #Spot if to get a more percise location
						print()
						print(itemDescription_dictionary[spot])
						print()
					else:
						print('\nThere is no item there.\n')
					break
			elif userChoice[0].upper() == 'Q': # If the userchoice's first letter captialized is Q
				return
			elif userChoice[0].upper() == 'D': # If the userchoice's first letter captialized is D
				sectionsTemp = 0
				for slot in range(0,len(inventory)): # Start of loop to display inventory
					part = inventory[sectionsTemp][0] # Part is to simplify looking at the print
					print(f"SLOT {sectionsTemp}: You have {inventory[sectionsTemp][1]} pieces of {itemID_dictionary[part]}.") # Displays inventory
					sectionsTemp += 1
		else:
			print('Invalid input.')