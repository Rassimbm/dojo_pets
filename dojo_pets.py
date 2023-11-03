class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        Pet.play()
        return self

    def feed(self):
        Pet.eat()
        return self

    def bathe(self):
        Pet.noise()
        return self
    
class Pet:
    def __init__(self , name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        