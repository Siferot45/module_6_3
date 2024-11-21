from Animal import Animal

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    
    def dive_in(self, dz):
        dz = abs(dz)