from typing import Any, Iterable, Optional
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode

class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            # last_index = self.len - 1
            last_node = self.tail  # добавить  tail после self step_by_step_on_nodes(last_index)
            self.linked_nodes(last_node, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.value == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next

        temp.next = None


    # def delete(self, value):
    #     # Delete a specific item
    #     current = self.head
    #     node_deleted = False
    #     if current is None:
    #         node_deleted = False
    #
    #     elif current.value == value:
    #         self.head = current.next
    #         self.head.prev = None
    #         node_deleted = True
    #
    #     elif self.tail.value == value:
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #         node_deleted = True
    #
    #     else:
    #         while current:
    #             if current.value == value:
    #                 current.prev.next = current.next
    #                 current.next.prev = current.prev
    #                 node_deleted = True
    #             current = current.next
    #
    #     if node_deleted:
    #         self.count -= 1

    def __len__(self):
        return len(self.elements)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

# class Node:
#     def __init__(self,initdata):
#         self.data = initdata
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return self.next
#
#     def setData(self,newdata):
#         self.data = newdata
#
#     def setNext(self,newnext):
#         self.next = newnext
#
# class UnorderedList:
#
#     def __init__(self):
#         self.head = None
#         self.count = 0

    # def append(self,item):
    #     current = self.head
    #     while current.getNext() != None:
    #         current = current.getNext()
    #     current.setNext(Node(item))
    def inser_at_beginning(self, item):
        new_Node = Node(item)
        new_Node.value(item)
        if self.len() == 0:
            self.head = new_Node
        else:
            new_Node.set_next(self.head)
            self.head = new_Node
#Method to insert at the end

def insertAtEnd(self, item):
    new_Node = Node(item)
    new_Node.setdata(item)
    current = self.head
    while current.getnext() != None:
        current = current.getnext()
    current.setnext(new_Node)
#Method to insert at the specified position

def insertAtPos(self, pos, item):
    if pos > self.listLength() or pos < 0:
        return None
    if pos == 0:
        self.inserAtBeginning(item)
    else:
        if pos == self.listLength():
            self.insertAtEnd(item)
        else:
            newNode = Node(item)
            newNode.setdata(item)
            current = self.head
            count = 0
            while count < pos - 1:
                count += 1
                current = current.getnext()
            newNode.setnext(current.getnext())
            current.setnext(newNode)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()


    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


# if __name__ == "__main__":
#     ll = DoubleLinkedList([1, 2, 3, 4, 5])
#
#     ll.clear()
#
#     print(ll)

#Sequence.register(D)

# def append_item(self, value):
#     # Append an item
#     new_item = Node(value, None, None)
#     if self.head is None:
#         self.head = new_item
#         self.tail = self.head
#     else:
#         new_item.prev = self.tail
#         self.tail.next = new_item
#         self.tail = new_item
#     self.count += 1
#
# def iter(self):
#     # Iterate the list
#     current = self.head
#     while current:
#         item_val = current.value
#         current = current.next
#         yield item_val