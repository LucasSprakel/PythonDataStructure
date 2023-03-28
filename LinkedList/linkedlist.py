class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    
    def list_is_empty(self):
        if self.size == 0:
            return True
        return False
    
    
    def insert(self, value, index):
        if index > self.size + 1 or index <= 0:
            raise IndexError("Invalid Index. Insira um indice válido, caso a lista por exemplo so tenha um elemento, não pode inserir no indice 3.")
        
        node = Node(value)
        
        if index == 1:
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(1, index-1):
                pointer = pointer.next
            node.next = pointer.next
            pointer.next = node
            
        self.size += 1

    
    def remove(self, index):
        if index > self.size or index <= 0:
            raise IndexError("Invalid Index. Para remover um elemento, a posição(indice) tem que existir")
        
        pointer = self.head
        aux = None
        for i in range(1, index):
            aux = pointer
            pointer = pointer.next
        
        aux.next = pointer.next

        self.size -= 1
    
    
    def show_element(self, index):
        if self.list_is_empty() or index > self.size or index <= 0:
            raise IndexError("Invalid Index")

        pointer = self.head
        for i in range(1, index):
            pointer = pointer.next
        
        print(pointer.value)

    
    def edit_element(self, index, value):
        if self.list_is_empty() or index > self.size or index <= 0:
            raise IndexError("Invalid Index")

        pointer = self.head
        for i in range(1, index):
            pointer = pointer.next

        pointer.value = value
        
    
    def show_list(self):
        pointer = self.head
        while pointer:
            print(pointer.value)
            pointer = pointer.next

