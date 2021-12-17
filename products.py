


class Products: 

	__name = ""
	__price = 0 
	__content = []

	def __init__(self, name, price) -> None:
		self.__name = name  
		self.__price = price
		self.__content.append(self) 

	def __str__(self):
		return self.DisplayProductsInfos() 

	def add(self):
		self.__content.append(self)

	def __iter__(self): 
		return iter(self.content)

	def __next__(self):
		return next(self.content)

	def getContent(self):
		return self.content

	def getName(self):
		return self.__name
	def getPrice(self): 
		return self.__price

	def setName(self, value): 
		self.__name = value

	def setPrice(self, value): 
		self.__price = value

	def DisplayProductsInfos(self):
		print(f"------------ Fiche produit pour {self.getName()} ------------------------")	
		for item in self.__dict__: 
			print(f"{item.replace('_Products__','').replace('_Drinks__','').replace('_Beers__','')} : {self.__dict__[item]}".replace("isCan : False", "Non disponible en canette").replace("isCan : True", "Disponible en canette").replace("isBottle : True", "En Bouteille").replace("isBottle : True", "Disponibe en Bouteille").replace("name :", "Nom :").replace("price :", "Prix :").replace("quantity :", "Quantité en cl :"))
		print ("-------------------------------")


class Drinks(Products): 
	__quantity = 0 # en cl
	__brand = ""  #Marque
	__isBottle = False 
	__isCan = False 	
	

	def __init__(self, name, price, quantity,  isB0ottle=False, isCan= False) -> None:
		super().__init__(name, price)

		self.__quantity = quantity 
		self.__isBottle = isB0ottle
		self.__isCan = isCan 
	


class Beers(Drinks): 
	
	__productionCountry = "" #pays de production 
	__alcoholLevel = 0.0 #Niveau d'alcool en % 
	__ingredients = [] #liste des ingrédients 
	__isTap = False 

	def getProductionCountry(self):
		return self.__productionCountry
	
	def getAlcoholLevel(self):
		return self.__alcoholLevel 
	
	def getIngredients(self): 
		return self.__ingredients 
	
	def getIsTap(self): 
		return self.__isTap
	

	def __init__(self, name, price, quantity, alcoholLevel) -> None:
		super().__init__(name, price, quantity, alcoholLevel)
		self.__quantity = quantity 
		self.__alcoholLevel = alcoholLevel 
		

class SoftDrinks(Drinks): 
	pass
AllProducts = []

chouffe = Beers("Chouffe", 2.5,75,8) 
chimayBleue = Beers("Chimay Bleue", 2.5, 33,9)
kasteelRouge = Beers("Kasteel rouge", 2, 33, 8)
tripleKarmeliet = Beers("Triple Karmeliet", 3.5,33, 8.4)
valDieuNoel = Beers("Val Dieu Noël ", 4, 33,7)


[AllProducts.append(item) for item in [chouffe, chimayBleue, kasteelRouge,tripleKarmeliet,valDieuNoel]]



coca = SoftDrinks("Coca-Cola", 1.50, 33,True, True)
fanta = SoftDrinks("Fanta", 1.50, 33,True, True)
tea = SoftDrinks("Iced-TEa", 1.25, 25,True, True)
eau = SoftDrinks("Eau", 2, 50,True,False)

[AllProducts.append(item) for item in  [coca, fanta, tea,eau]]

if __name__ == '__main__': 
	coca.DisplayProductsInfos()
	chouffe.DisplayProductsInfos()

