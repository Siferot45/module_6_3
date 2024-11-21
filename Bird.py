from Animal import Animal
import random

class Bird(Animal):
    
    beak = True
    
    def lay_eggs(self):
        number = random.randint(1, 4)
        print(f'Here are(is) {number} eggs for you')