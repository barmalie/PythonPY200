from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next  # вызовется setter

    def __repr__(self) -> str:
        # next_repr = str(None) if self.next is None else f"DoublincedNode{self.next.value},{None},{None}"
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self.next = next

class DoubleLinkedNode(Node):
    def __init__(self, value, next=None, prev=None):
        super().__init__(value, next)
        #self.value = value
        #self.next = next
        self.prev = prev
        # next += Node
        # prev -= Node

    def __repr__(self) -> str:

        next_repr = str(None) if self.next is None else f"DoublinkedNode{self.next.value},{None},{None}"
        last_repr = str(None) if self.prev is None else f"DoublinkedNode{self.prev.value},{None},{None}"
        # return f"Node({self.value}, {None})" if self.next and self.prev is None else f"Node({self.value}, Node({self.next}))"
        return f"DoubleLinkedNode({self.value},{next_repr},{last_repr})"

    # +репр перегружаем
    def __str__(self) -> str:
        return str(self.value)


    # +стр наследуем

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    # +из валид перзагружаем , делаем через метод класс в classmethod

    @property
    def next(self):
        return self.next, self.prev

    @next.setter
    def next(self, next_: Optional["Node"], prev: Optional["Node"]):
        self.is_valid(next_)
        self.next = next
        self.prev = prev

    # +геттеры и сеттеры наследуются

    # +prev  по образу и подобию некста


(DoubleLinkedNode(2, None, None))
