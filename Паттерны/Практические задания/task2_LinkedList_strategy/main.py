from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  # TODO наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver# TODO расширяем конструктор, чтобы в связном списке был driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        self.clear()# TODO считать данные из драйвера
        data = self.driver.read()
        for value in data:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)# TODO записать данные с помощью драйвера



if __name__ == '__main__':
    ll = LinkedListWithDriver()  # TODO инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    driver_1 = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver_1
    ll.read()# TODO инициализировать драйвер и считать данные
    print(ll)

    print("Записать данные в файл по умолчанию")
    driver_2 = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver_2
    ll.write()
    print(ll)
