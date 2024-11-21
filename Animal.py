class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    
    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]
        
    def speak(self):
        print(f"{self.sound}")
        
    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")
            
    def move(self, dx, dy, dz):
        new_z_axis = self._cords[2] + dz * self.speed
        
        if new_z_axis < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z_axis
            
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")