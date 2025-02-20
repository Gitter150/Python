class doublyLinkedList:
    class Node:
        def __init__(self, x):
            self.data = x
            self.next = None
            self.prev = None
    def __init__(self):
        self.head = None
        self.tail = None
    def push_front(self, x: int):
        newNode = self.Node(x)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        
    def push_back(self, x: int):
        newNode = self.Node(x)
        newNode.prev = self.tail
        if self.tail is not None:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode

    def display(self):
        if self.head is None:
            print("Error! List is empty. Can't print empty list.")
            return
        curr = self.head
        while curr is not None:
            print(f"{curr.data}", end = "" if curr.next is None else " -> ")
            curr = curr.next
        print()
    
if __name__ == "__main__":
    lst = doublyLinkedList()
    for x in range(5):
        lst.push_back(x+1)
    lst.display()

        


