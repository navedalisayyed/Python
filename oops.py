#inheritance

class car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
        #self.drive()
    def drive(self):
        print(f"The person will drive the {self.enginetype} car")

class Tesla(car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving=is_selfdriving
        self.selfdriving()
    def selfdriving(self):
        print(f"Testla supports self driving {self.is_selfdriving}")    

tesla1=Tesla(4,5,"electric",True)   

##Multiple inheritance

class Animal:  ##Base class 1
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Subclasses must implement this method")    

class Pet:   ##Base class 2
    def __init__(self,owner):
        self.owner=owner

##Derive class

class Dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    def speak(self):
        return f"{self.name} says woof"   

 ##create an object

dog=Dog("Buddy","Krrish") 
print(dog.speak())      
             

              
        




        
