import doctest


class Pencil:
    def __init__(self, colored: bool, sharpness: float):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param colored: цвет карандаша
        :param sharpness: Наточенность карандаша (состояние от 0 (ненаточен) до 1 (наточен))

        Примеры:
        >>> pencil = Pencil(True, 0.5)  # инициализация экземпляра класса
        """
        if not isinstance(sharpness, (int, float)):
            raise TypeError("Наточенность карандаша должна быть типа int или float")
        if not (0 <= sharpness <= 1):
            raise ValueError("Наточенность карандаша должна быть  числом от 0 до 1")
        self.sharpness = sharpness

        if not isinstance(colored, bool):
            raise TypeError("Карандаш может быть либо цветной (True) либо простой (False)")
        self.colored = colored

    def is_pencil_sharpened(self) -> bool:
        """
        Функция которая проверяет наточен ли карандаш

        :return: Наточен ли карандаш

        Примеры:
        >>> pencil = Pencil(False, 1)
        >>> pencil.is_pencil_sharpened()
        """
        ...

    def write_text(self, text: str) -> None:
        """
        Написание текста с помощью карандаша.
        :param text: Текст который мы хотим написать

        :raise ValueError: Если текст слишком длинный, то карандаша нам не хватит и он затупится, вызываем ошибку

        Примеры:
        >>> pencil = Pencil(True, 0.8)
        >>> pencil.write_text("Привет мир!")
        """
        if self.sharpness < 0.5:
            raise Exception("Наточите карандаш!")
        if not isinstance(text, str):
            raise TypeError("Текст должен быть типа str")
        if len(text) > 1000:
            raise ValueError("Текст слишком длинный, лучше использовать ручку")
        ...

    def sharpening(self) -> None:
        """
        Заточка карандаша

        :raise Exception: Если карандаш уже заточен, заточить снова его не получится


        Примеры:
        >>> pencil = Pencil(True, 0.5)
        >>> pencil.sharpening()
        """
        if self.sharpness == 1:
            raise Exception("Карандаш уже наточен")
        ...


class Energetic:
    def __init__(self, is_open: bool, volume: int, fullness: int):
        """
        Создание и подготовка к работе объекта "Энергетик"

        :param is_open: открыт ли энергетик
        :param volume: объём банки энергетика (мл)
        :param fullness: наполненность банки энергетиком (мл)


        Примеры:
        >>> python_enerjy = Energetic(False, 500, 500)  # инициализация экземпляра класса
        """
        if not isinstance(is_open, bool):
            raise TypeError("Энергетик может быть либо Открыт (True) либо Закрыт (False)")
        self.is_open = is_open

        if not isinstance(volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int")
        if volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.volume = volume

        if not isinstance(fullness, (int, float)):
            raise TypeError("Наполненость жидкостью должно быть int")
        if fullness < 0:
            raise ValueError("Наполненость жижкостью не может быть отрицательным числом")
        self.fullness = fullness

        if is_open is False and volume != fullness:
            raise Exception("Бракованная бутылка")
        if fullness > volume:
            raise Exception("В бутылку нельзя поместить больше чем она по объёму")

    def open_bottle(self) -> None:
        """
        Открыть бутылку, чтобы из неё можно пить

        :raise Exception: Если бутылка открыта, её уже не получится открыть

        Примеры:
        >>> red_bool = Energetic(False, 330, 330)
        >>> red_bool.open_bottle()
        """
        if self.is_open is True:
            raise Exception("Бутылка уже открыта")
        ...

    def drinking(self, volume_consumed: int) -> None:
        """
        Выпить необходимое количество напитка

        :param volume_consumed: какое количество мы хотим выпить (мл)
        Примеры:
        >>> adrenaline_push = Energetic(True, 500, 500)
        >>> adrenaline_push.drinking(300)
        """
        if not isinstance(volume_consumed, int):
            raise TypeError("Выпитый объём должен быть int")
        if volume_consumed <= 0:
            raise ValueError("Выпитый объём должен быть положительным числом")
        if volume_consumed > self.fullness:
            raise ValueError("Выпитый объём не должен превышать объёма наполнености бутылки")
        if self is False:
            raise Exception("Чтобы выпить, нужно открыть бутылку")
        ...


class Ball:
    def __init__(self, size_ball: int, inflated: bool):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param size_ball: Размер мяча
        :param inflated: Накаченность мяча (накачен или нет)

        Примеры:
        >>> football_ball = Ball(5, True)  # инициализация экземпляра класса
        """
        if not isinstance(size_ball, int):
            raise TypeError("Размер мяча должен быть типа int")
        if not (1 <= size_ball <= 10):
            raise ValueError("Размер мяча должен быть числом от 0 до 1")
        self.size_ball = size_ball

        if not isinstance(inflated, bool):
            raise TypeError("Мяч может быть либо накачан (True) либо спущен (False)")
        self.inflated = inflated

    def pump_up(self) -> None:
        """
        Накачать мяч

        :raise Exception: Если мяч уже накачан, накачать снова его не получится


        Примеры:
        >>> volleyball_ball = Ball(6, False)
        >>> volleyball_ball.pump_up()
        """
        if self.inflated is True:
            raise Exception("Мяч уже накачан")
        ...

    def get_volume(self) -> float:
        """
        Вычислить объём мяча по его размеру

        :return: объём мяча (в дм куб.)

        Примеры:
        >>> basketball_ball = Ball(7, True)
        >>> basketball_ball.get_volume()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
