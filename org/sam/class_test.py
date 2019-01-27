

class City:
    
    def __init__(self, name, population):
        self.name = name
        self.population = population 
        
       
    def get_first_letter(self):
        return self.name[0]
        
    def get_last_letter(self):
         return self.name[-1]   

    

cityObj = City("Toronto", 16)

print(cityObj.name)

print(cityObj.get_first_letter())

print(cityObj.get_last_letter())