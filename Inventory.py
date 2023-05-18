
itemID_dictionary = {100: "Dirt", 101: "Brick", 102: "Wood"}
itemDescription_dictionary = {"Dirt": 'A handful of dirt.', "Brick": 'Used in some buildings. Seems to made of clay.', "Wood": 'A log of wood.'}

def inventory(inventory, itemID, amount):
	from Menus import information as M#, testing as test   # This is just importing the class information
	sections = 0   # This is used to get the section area
	notIn = 0   # This is a var to count if its not in
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
		print(M.inventory)   # prints Inventory

def printInventory(inventory):
	from Menus import information as M
	sections = 0
	sections2 = 0
	for slot in range(0,len(inventory)):
		part = inventory[sections][0]
		print(f"SLOT {sections+1}: You have {inventory[sections][1]} pieces of {itemID_dictionary[part]}.")
		sections += 1
	valid = False
	while not valid:

		userChoice = input('''
	Inventory
-----------------
L - Look at item
Q - Quit

''')
		if userChoice[0].upper() == 'L':
			valid2 = False
			while not valid2:
				userChoice2 = int(input('\nWhat item do want to look at.\n'))
				while userChoice2 not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50):
					print('Must be number.')
					userChoice2 = int(input('\nWhat item do want to look at.\n'))
				if userChoice2 in range(0, len(inventory)):
					spot = itemID_dictionary[inventory[userChoice2-1][0]]
					print()
					print(itemDescription_dictionary[spot])
					print()
				else:
					print('\nThere is no item there.\n')
				break
		elif userChoice[0].upper() == 'Q':
			return