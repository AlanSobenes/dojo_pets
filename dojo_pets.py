class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Draco","Dragon", "Firebreath")
    
    def walk(self):
        self.pet.play()
        print("Walkin my Dragon")
        

    def feed(self):
        self.pet.eat()
        print("Draco is fed")
        

    def bathe(self):
        self.pet.noise()
        print("Giving Draco a bath")
        

class Pet:
    def __init__(self, name, pettype, tricks):
        self.name = name
        self.type = pettype
        self.tricks = tricks
        self.health = 20
        self.energy = 50
    
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

    def noise(self):
        print(f"{self.name} Growled Really Loud!")
        
ryu = Ninja("Ryu", "Hoshi", "humans", "cattle" )



ryu.walk()
ryu.bathe()
ryu.feed()
