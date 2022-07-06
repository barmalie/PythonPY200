class  node (object):
    def __init__ (self,data):
        self.data = data
        self.next = None
class lk (object):
    def __init__ (self):
        self.current_data = None
        self.header = None
    def add (self,data):
        New_node = node (data)
        New_node.next = self.current_data
        self.current_data = New_node
        self.head = self.current_data
    def display (self):
        #print 'coming to display', self.current_data
        self.current_data = self.head
        while (self.current_data is not None):
            print(self.current_data.data)
            self.current_data = self.current_data.next
    def remove (self,value):
        self.value = value
        present_node = self.head
        self.current_data = self.head

        while self.current_data is not None:
            if self.head == self.value:
                self.head = self.head.next
            else:
                #k = self.current_data.next
                #print k.data
                print(self.current_data.data)
                print(self.current_data.next)

            self.current_data = self.current_data.next

k = lk()
k.add (3)
k.add(4)
k.add(5)
k.display()
k.remove(4)
k.display