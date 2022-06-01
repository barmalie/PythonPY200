from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("некорректный тип данных")
        if capacity_volume <= 0:
            raise ValueError("недопустимое значение")# raise останавливает программу
        self.capacity = capacity_volume
        self.occupied_volume = occupied_volume  # TODO инициализировать объект "Стакан"


    def is_glass(self) -> bool:
        self.capacity_volume = 34
        self.occupied_volume = 23  # TODO инициализировать объект "Стакан"
        print(type(Glass))


if __name__ == "__main__":
    glass1 = Glass(23, 34)
    print(glass1)
    glass3 = Glass(23.4, 23)
    print(glass3)
    glass2 = Glass(-34, 23)
    print(glass2)

# TODO попробовать инициализировать не корректные объекты
