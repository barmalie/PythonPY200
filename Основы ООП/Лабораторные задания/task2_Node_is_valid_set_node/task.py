from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_ # работает без двух нижних строчек
        # self.next = None
        # self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(self.next, node, type(None)):
            raise TypeError

        # TODO метод проверки корректности связываемого узла


    def set_next(self, next_: Optional["Node"] = None) -> None:
        # TODO метод должен проверять корректность узла и устанавливать значение атрибуту next
        self.is_valid(next_)
        self.next = next_


if __name__ == '__main__':
    # TODO инициализируйте два узла с любыми значеними
    first_node = Node(1)
    second_node = Node(2)
    first_node.next = second_node
    # TODO свяжите первый узел со вторым

    print(first_node)
    print(second_node)
