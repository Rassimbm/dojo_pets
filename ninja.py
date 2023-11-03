from pet import Pet
class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} is feeding {self.pet.name}")
        return self

    def bathe(self):
        self.pet.make_noise()
        return self
    
mr_squeaky = Pet("Mr Squeaky" , "Cat" , "Speak" , "Murmuring")

ninja_1 = Ninja("Rassim" , "Benmhamed" , "jerky beef" , "Salmon" , mr_squeaky )

ninja_1.walk().feed().bathe()