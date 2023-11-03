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
        
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        return f"{self.name} is being noisy!!!"