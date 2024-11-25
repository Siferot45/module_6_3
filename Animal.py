class Animal:
    """
    Базовый класс для представления животного.

    Содержит общие атрибуты и методы, которые могут быть расширены в дочерних классах для конкретных типов животных.
    Животное может двигаться, издавать звуки, атаковать и возвращать свои текущие координаты.

    Атрибуты класса:
        live (bool): Указывает, живо ли животное (по умолчанию True).
        sound (str): Звук, издаваемый животным (по умолчанию None).
        _DEGREE_OF_DANGER (int): Уровень опасности животного (по умолчанию 0, от 0 до 10).
    
    Атрибуты экземпляра:
        speed (int or float): Скорость движения животного.
        _cords (list): Текущие координаты животного в формате [x, y, z].
    """

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        """
        Инициализация объекта Animal.

        Устанавливает начальную скорость и координаты животного.

        Аргументы:
            speed (int or float): Скорость движения животного.
        """
        self.speed = speed
        self._cords = [0, 0, 0]  # Начальные координаты животного

    def speak(self):
        """
        Издает звук, присущий животному.

        Если звук не установлен (sound == None), ничего не выводится.
        """
        if self.sound:
            print(f"{self.sound}")
        else:
            print("The animal is silent.")

    def attack(self):
        """
        Пытается атаковать.

        Поведение зависит от уровня опасности животного (_DEGREE_OF_DANGER):
        - Если уровень опасности >= 5, животное атакует.
        - Если уровень опасности < 5, животное остается мирным.
        """
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")
        else:
            print("Sorry, I'm peaceful :)")

    def move(self, dx, dy, dz):
        """
        Перемещает животное в пространстве.

        Учитывается скорость движения животного, а также ограничение на движение по оси Z:
        животное не может погружаться ниже нуля.

        Аргументы:
            dx (int or float): Смещение по оси X.
            dy (int or float): Смещение по оси Y.
            dz (int or float): Смещение по оси Z.

        Возвращает:
            None
        """
        new_z_axis = self._cords[2] + dz * self.speed

        if new_z_axis < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z_axis

    def get_cords(self):
        """
        Возвращает текущие координаты животного.

        Координаты выводятся в формате:
        "X: <значение> Y: <значение> Z: <значение>".

        Возвращает:
            None
        """
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")
