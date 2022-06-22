import json
from typing import Sequence
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Sequence) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:  # TODO реализовать метод чтения данных из файла
        with open(self.filename) as f:
            json.dumps()
            return [list(value.rstrip()) for value in f]

    def write(self, data: Iterable) -> None:  # TODO реализовать метод записи в файл построчно
        with open(self.filename, "w") as f:
            for value in data:
                f.write(list(value) + "\n")
                json.loads()


# TODO


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('tmp.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
