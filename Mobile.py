""" Mobile unit - mobilná jednotka, všetko čo sa pohybuje """


class Mobile:
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self, var):
		self.__name = var
	
	@property
	def AR(self):
		return self.__dr
		
	@AR.setter
	def AR(self, var):
		self.__ar = var

	@property
	def DR(self):
		return self.__dr
		
	@DR.setter
	def DR(self, var):
		self.__dr = var
	
	@property
	def hp(self):
		return self.__hp
		
	@hp.setter
	def hp(self, var: int):
		self.__hp = var
	
	def __init__(self, name: str, hp: int, AR: int, DR: int):
		self.__name = name
		self.__hp = hp
		self.__AR = AR
		self.__DR = DR
	
	def damage(self, amount: int):
		self.__hp -= amount
		print(self.__hp)
