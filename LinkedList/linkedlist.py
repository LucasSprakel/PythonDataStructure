class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def list_is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def insert(self, value, index):
        if index > self.size + 1 or index <= 0:
            raise IndexError("Invalid Index")
        
        node = Node(value)
        
        if index == 1:
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(1, index-1):
                pointer = pointer.next
            pointer.next = node
            pointer = node
        
        self.size += 1
            

    def show_element(self, index):
        if self.list_is_empty() or index > self.size or index <= 0:
            raise IndexError("Invalid Index")

        pointer = self.head
        for i in range(1, index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("error")
        
        if pointer:
            return pointer.value
        else:
            raise IndexError("error")
        
    
    def show_list(self):
        pointer = self.head
        while pointer:
            print(pointer.value)
            pointer = pointer.next

    
lista = List()
lista.insert(50, 1)
lista.insert(30, 2)
lista.insert(40, 3)
lista.insert(60, 4)
lista.insert(80, 3)
lista.insert(70, 2)
lista.show_list()
    

