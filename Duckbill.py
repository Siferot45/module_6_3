from AquaticAnimal import AquaticAnimal
from Bird import Bird
from PoisonousAnimal import PoisonousAnimal

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    """
    Класс для представления утконоса, который наследует свойства птиц, ядовитых и водных животных.

    Утконос уникален тем, что обладает характеристиками из нескольких классов:
    - Как птица, имеет клюв и может откладывать яйца.
    - Как ядовитое животное, может быть опасным.
    - Как водное животное, способен погружаться под воду.
    
    Атрибуты класса:
        sound (str): Звук, издаваемый утконосом ("Click-click-click").
    
    Методы:
        __init__(speed): Инициализирует объект утконоса с заданной скоростью.
    """
    sound = "Click-click-click"

    def __init__(self, speed):
        """
        Инициализация объекта Duckbill.

        Устанавливает скорость утконоса и вызывает конструкторы родительских классов.

        Аргументы:
            speed (int or float): Скорость движения утконоса.
        """
        super().__init__(speed)
