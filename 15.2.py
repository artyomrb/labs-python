class Animal:
    name = ""
    def __init__(self, newName):
        self.name = newName
        print("Родилось животное ", self.name)

    def setName(self, newName):
        self.name =  newName

    def getName(self):
        return self.name

    def eat(self):
        print("Ням-ням")
    def makeNoise(self):
        print(self.name, "говорит Гррр")




myAnimal=Animal("Шарик")
print("Имя животного - ", myAnimal.getName())
myAnimal.setName("Тузик")
print("Теперь имя животного - ", myAnimal.getName())
myAnimal.makeNoise()
myAnimal.eat()

