from Bird import Bird
from PoisonousAnimal import PoisonousAnimal

class Duckbill(Bird, PoisonousAnimal):

    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)
