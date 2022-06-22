from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver, JsonFileDriver


class DriverFactoryMethod(ABC):
    @classmethod
    @abstractmethod
    def get_driver(cls) -> IStructureDriver:
        ...


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.json)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'

        return JsonFileDriver(filename)


#class JsonFileDriverFactoryMethod(DriverFactoryMethod):# TODO реализовать класс JsonFileDriveFactoryMethod


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()
    print(driver)
