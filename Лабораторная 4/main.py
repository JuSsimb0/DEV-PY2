import doctest
from typing import Union


class FlyingVehicle:
    """Базовый класс для летательных аппаратов."""

    def __init__(self, name: str, max_speed: float, weight: int):
        """
        Иницилизация объекта "летательный аппарат"


             :param name (str): Название летательного аппарата.
             :param max_speed (float): Максимальная скорость летательного аппарата.
             :param weight (int): Вес летательного аппарата.
        """
        self.name_ = name
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        self.max_speed_ = max_speed

        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        self.weight_ = weight

    def __str__(self) -> str:

        return f"Летательное устройство '{self.name_}'"

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}(name='{self.name_}', max_speed={self.max_speed_})"


class Airplane(FlyingVehicle):
    """Класс "Самолёт" (На основе класса "Летательное устройство")."""

    def __init__(self, name: str, max_speed: float, weight: int, wingspan: float):
        """
         Иницилизация объекта "Самолёт"


        :param  name (str): Название самолета.
        :param  max_speed (float): Максимальная скорость самолета.
        :param weight (int): Вес самолёта.
        :param  wingspan (float): Размах крыльев самолета.

        """
        super().__init__(name, max_speed, weight)
        if not isinstance(wingspan, (int, float)):
            raise TypeError("Размах крыльев должен быть типа int или float")
        self.wingspan_ = wingspan

    def __str__(self) -> str:
        return f"{super().__str__()} (Самолёт) с размахом крыльев {self.wingspan_} метров."

    def __repr__(self) -> str:

        return f"{super().__repr__()[:-1]}, wingspan={self.wingspan_})"

    def take_off(self, runway_length: float) -> Union[str, bool]:
        """
     взлет самолета.


       runway_length (float): длина взлетно-посадочной полосы, необходимая для взлета.

        :return    Union[str, bool]: Сообщение, указывающее, был ли взлет успешным или нет.

        """
        if runway_length >= 1.5 * self.weight_ * self.wingspan_:
            return "Успешный взлет!"
        else:
            return False


class Helicopter(FlyingVehicle):
    """Класс, представляющий вертолет."""

    def __init__(self, name: str, max_speed: float, weight: int, num_rotors: int):
        """



        :param    name (str): Название вертолёта.
        :param    max_speed (float): Максимальная скорость вертолёта.
        :param    weight (int): Вес вертолёта.
        :param    num_rotors (int): Количество несущих винтов вертолета.
        """
        super().__init__(name, max_speed, weight)
        self.num_rotors_ = num_rotors

    def __str__(self) -> str:

        return f"{super().__str__()} (Вертолёт) c общим числом винтов: {self.num_rotors_}."

    def hover(self) -> str:
        """
        Вертолёт находится в состоянии зависания в воздухе.

        :return    str: Сообщение о том, что вертолет завис.
        """

        return "Вертолет сейчас завис в воздухе."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации