class Products: 

	__name = ""
	__price = 0 

	def __init__(self, name, price) -> None:
		self.__name = name  
		self.__price = price 

	def getName(self):
		return self.__name
	def getPrice(self): 
		return self.__price

	def setName(self, value): 
		self.__name = value

	def setPrice(self, value): 
		self.__price = value

class Beers(Products): 
	
	__quantity = 0 # en cl
	__brand = ""  #Marque 	
	__productionCountry = "" #pays de production 
	__alcoholLevel = 0.0 #Niveau d'alcool en % 
	__ingredients = [] #liste des ingrédients 
	__tap = False 
	__bottle = False 
	__can = False 

	def __init__(self, name, price, quantity, alcoholLevel) -> None:
		super().__init__(name, price)
		self.__quantity = quantity 
		self.__alcoholLevel = alcoholLevel 

class SoftDrinks(Products): 

	__quantity = 0 
	__brand = "" 


chouffe = Beers("Chouffe", 4.5,75,8) 

print(chouffe.getName(), chouffe.getPrice())

if __name__ == '__main__': 
	__name__()
