from task import DoubleLinkedNode


def test_repr_double():
    """

    :return:
    """
    node = DoubleLinkedNode(5)
    expected_value = "DoubleLinkedNode(5, None,None)"
    actual_value = repr(node)
    assert expected_value == actual_value


def test_repr_double2():
    """

    :return:
    """
    next_node = DoubleLinkedNode(3)
    current_node = DoubleLinkedNode(2)

    current_node.next = next_node
    next_node.prev = current_node

    expected_value = "DoubleLinkedNode(2,DoubleLinkedNode(3, None,None), None)"
    actual_value = repr(current_node)

    assert expected_value == actual_value

if __name__ == "__main__":
    test_repr_double()
    test_repr_double2()