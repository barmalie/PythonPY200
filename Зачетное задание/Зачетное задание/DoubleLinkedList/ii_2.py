class  node (object):
    def __init__ (self,data):
        self.data = data
        self.next = None

class lk (object):
    def __init__ (self):
        self.current_data = None
        self.header = None
    def add (self,data):
        New_node = node(data)
        New_node.next = self.current_data
        self.current_data = New_node
        self.head = self.current_data
    def display (self):
        #print 'coming to display', self.current_data
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    def remove (self,value):
        current_node = self.head
        if current_node.data == value:
            self.head = current_node.next
            return
        while current_node.next is not None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next

k = lk()
k.add (3)
k.add(4)
k.add(5)
k.display()
k.remove(4)
print("Hmm")
k.display()