class Pet:

    def __init__(self, name):
        self.name = name

    def say(self):
        return "{0}: -----".format(self.name)


class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

class FightingDog(Dog):

    def __init__(self, name, breed, is_angry):
        super().__init__(name, breed)
        self.is_angry = is_angry

    def say(self):
        return super().say() + 30*'waw' if self.is_angry else super().say()

    def feed(self):
        self.is_angry = False
    
    def step_on_tail(self):
        self.is_angry = True

class Crocodile(Pet):
    
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

        
    
dog = FightingDog("Кузя", "Овчарка", False)

# for i in range(10):
#     if i % 2 == 1:
#         dog.step_on_tail()
#     else:
#         dog.feed()

#     print(dog.say())

croc = Crocodile("Боря", 73)
print(croc.say())
