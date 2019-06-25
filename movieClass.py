#Movie Class for instantiating objects

class Movie:

    def __init__ (self,name,category,description,price):
        self.name=str(name)
        self.category=str(category)
        self.description=str(description)
        self.price=price

    def getName(self):
        return self.name    


    def getCategory(self):
        return self.category

    def getDescription(self):
        return self.description 
    
    def getPrice(self):
        return self.price
    
    def getPriceWithGST(self):
        return self.price*1.07

    def setName(self,name):
        self.name=name 

    def setCategory(self,category):
        self.category=category

    def setDescription(self,description):
        self.description=description

    def setPrice(self,price):
        self.price=price            