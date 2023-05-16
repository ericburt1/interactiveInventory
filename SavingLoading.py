

class InfoToSave(object):

	def __init__(self):
		self.__inventory = ((100, 0))
	
	@property
	def inventory(self):
		return self.__inventory

