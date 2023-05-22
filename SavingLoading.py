

class InfoToSave(object):

	def __init__(self):
		self.__inventory = []
		self.__bagSize = 1 # bag sizes go from 1 - 10 you multiply the size by five to get the inventory size
	
	@property   # Just a random proprty setter just in case
	def inventory(self):
		return self.__inventory

	@property   # Just a random proprty setter just in case
	def bagSize(self):
		return self.__bagSize
