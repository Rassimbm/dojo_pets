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
    
class Dog(Pet):
    def __init__(self , name , type , tricks , noise):
        super().__init__(name , type , tricks, noise)
