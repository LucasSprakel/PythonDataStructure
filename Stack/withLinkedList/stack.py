class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  

    
    def stack_is_empty(self):
        if self.size == 0:
            return True
        return False     
    

    def push(self, value):
        node = Node(value)
        
        node.next = self.top
        self.top = node

        self.size += 1

    
    def pop(self):
        if self.top is None:
            raise Exception("A pilha está vazia")
        
        last_node = self.top
        self.top = self.top.next
        last_node.next = None

        self.size -= 1
        
        return last_node.value
    

    def display(self):
        if self.top is None:
            print("A pilha está vazia.")
        else:
            current = self.top
            while current is not None:
                print(current.value)
                current = current.next

    