
itemID_dictionary = {100: "dirt"}

def inventory(itemID, amount):
	from Menus import information as M
	itemInThingy = False
	for j in range(0, len(M.inventory)):
		if itemID == M.inventory(j)(0):
			itemInThingy = True
		else:
			print(f'Not in slot {j}.')
			print(itemID)
			print(M.inventory(j))
	if itemInThingy == True:
		for i in M.inventory:
			if M.inventory(i) == itemID_dictionary[itemID]:
				M.inventory(i) == amount
	'''
from Menus import information as M

itemID_dictionary = {100: "dirt"}

def inventory(itemID, amount):
	itemInThingy = False
	for j in range(0, len(M.inventory)):
		if itemID == M.inventory[j][0]:
			itemInThingy = True
		else:
			print(f'Not in slot {j}.')
			print(itemID)
			print(M.inventory[j])
	if itemInThingy:
		for i in range(len(M.inventory)):
			if M.inventory[i] == itemID_dictionary[itemID]:
				M.inventory[i] = amount


	else:
		alreadyInInventory = False
		itemsToAdd = [itemID, amount]
		placeIn = 0
		for i in range(0, len(M.inventory)):
            if itemID in M.inventory[placeIn:0]:
				alreadyInInventory = True
			placeIn += 1
		if alreadyInInventory == False:
			M.inventory.append(itemsToAdd)
	print(M.inventory)
	'''

# I want to check if the item ID is in the inventory and if it is then just change the amount else