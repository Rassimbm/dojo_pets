class Pet:
    def __init__(self , name , type , tricks , noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def make_noise(self):
        print(self.noise)
        return self
    
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