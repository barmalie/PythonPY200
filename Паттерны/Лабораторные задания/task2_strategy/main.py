from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod, JsonFileDriverFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, driver):
        print("вызван setter")
        self._driver = driver
    # TODO свойство для driver (getter + setter)

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self.driver.read()
        for value in data_from_driver:
            self.append(value)



    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        #self.driver.write(self)
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value) + "\n")

if __name__ == '__main__':
    ll = LinkedListWithDriver()
    driver_1 = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver_1  # TODO инициализировать SimpleFileDriver
    ll.read()
    print(ll)

    driver_2 = JsonFileDriverFactoryMethod.get_driver()
    ll.driver = driver_2  # TODO инициализировать JsonFileDriver
    ll.write()



