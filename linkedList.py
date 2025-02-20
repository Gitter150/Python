class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, x):
            self.data = x
            self.next = None
            self.prev = None

    def push_front(self, x: int):
        newNode = self.Node(x)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        self.size += 1
        
    def push(self, x: int):
        newNode = self.Node(x)
        newNode.prev = self.tail
        if self.tail is not None:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.size += 1

    def pop_front(self):
        if self.size < 1:
            print("Error! List is empty. Can't remove any element.")
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        firstNode = self.head
        firstNode.next.prev = None
        self.head = firstNode.next
        firstNode.next = None
        firstNode = None
        self.size -= 1
    
    def pop(self):
        if self.size < 1:
            print("Error! List is empty. Can't remove any element.")
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            size -= 1
            return
        lastNode = self.tail
        lastNode.prev.next = None
        self.tail = lastNode.prev
        lastNode.prev = None
        lastNode = None
        self.size -= 1
    
    def find(self, x:int) -> int:
        curNode = self.head 
        i = 0
        while curNode is not None:
            if curNode.data == x:
                return i
            curNode = curNode.next
            i += 1
        return -1

    def reverse(self):
        if self.size <= 1:
            return
        curNode = self.head
        while curNode is not None:
            curNode.prev, curNode.next = curNode.next, curNode.prev
            curNode = curNode.prev
        self.head, self.tail = self.tail, self.head
           
    def display(self):
        if self.head is None:
            print("Error! List is empty. Can't print empty list.")
            return
        curr = self.head
        while curr is not None:
            print(f"{curr.data}", end = "" if curr.next is None else " <-> ")
            curr = curr.next
        print()
    
if __name__ == "__main__":
    dll = doublyLinkedList()
    for x in range(5):
        dll.push(x+1)
    dll.display()
    print(dll.find(1))
        


