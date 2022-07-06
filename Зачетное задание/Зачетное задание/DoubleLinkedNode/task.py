# БАЗОВЫЙ УЗЕЛ ДЛЯ ОДНОСВЯЗНОГО СПИСКА
# ASSERT
# PYTEST
from typing import Any, Optional

class Node:
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = None
        self.set_next(next_)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self._next is None else f"Node({self.value}, Node({self._next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError



class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self, prev) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"

    def __str__(self) -> str:
        return str(self.value)

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"





#if __name__ == "__main__":

