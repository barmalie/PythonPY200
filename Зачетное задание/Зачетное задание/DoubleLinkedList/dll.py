from collections.abc import MutableSequence

class LinkedList(MutableSequence):
    class _Node:
        def __init__(self, value, _next=None, _last=None):
            self.value, self._next, self._last = value, _next, _last

        def __str__(self):
            return f'Node({self.value})'

    def __init__(self, iterable=()):
        self.start = None
        self.last = None

        empty = object()
        iterable = iter(iterable)
        first = next(iterable, empty)

        if first is empty:
            return

        current = self._Node(first)
        self.start, self.last = current, current

        for value in iterable:
            new_node = self._Node(value, _last=self.last)
            self.last._next = new_node
            self.last = new_node


    def __len__(self):
        if self.start is None:
            return 0
        else:
            return sum(1 for _ in self)

    def __iter_nodes(self):
        current = self.start

        while current is not None:
            yield current
            current = current._next

    def __reversed_iter_nodes(self):
        current = self.last

        while current is not None:
            yield current
            current = current._last

    def __iter__(self):
        for node in self.__iter_nodes():
            yield node.value

    def __reversed__(self):
        for node in self.__reversed_iter_nodes():
            yield node.value

    def __get_node(self, index):
        if index >= 0:
            for item in self.__iter_nodes():
                if index == 0:
                    return item
                index -= 1
        else:
            for item in self.__reversed_iter_nodes():
                if index == 0:
                    return item
                index += 1
        raise IndexError

    def __getitem__(self, index):
        if index >= 0:
            for item in self:
                if index == 0:
                    return item.value
                index -= 1
        else:
            for item in reversed(self):
                if index == 0:
                    return item.value
                index += 1
        raise IndexError

    def __setitem__(self, key, value):
        self[key].value = value

    def __delitem__(self, key):
        node = self[key]
        if node._last:
            node._last._next = node._next
        if node._next:
            node._next._last = node._last

    def insert(self, index, value):
        if index > len(self):
            self.last = self._Node(value, _last=self.last)
        else:
            where = self.__get_node(index)
            _last = where._last
            new_node = self._Node(value, _next=where, _last=_last)
            if _last:
                _last._next = new_node
            else:
                self.start = new_node

            where._last = new_node

ll = LinkedList(range(1, 5))
print(*ll)

print(*reversed(ll))

ll.insert(2, 'foo')
print(*ll)