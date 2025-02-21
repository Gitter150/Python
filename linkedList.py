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

    def dataAt(self, x: int) :
        if not (0<=x<self.size):
            raise ValueError("Invalid Index. Please enter a valid index")
        curNode = None
        if x < self.size / 2:
            i = 0
            curNode = self.head
            while curNode.next and i < x:
                curNode = curNode.next                 
                i += 1 
        else:
            i = self.size - 1
            curNode = self.tail
            while curNode.prev and i > x:
                curNode = curNode.prev
                i -= 1
        return curNode.data
        
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
    dll.push(5)
    dll.push(0)
    dll.push(2)
    dll.push(9)
    dll.push(6)
    dll.display()
    print(dll.find(1))
    print(dll.dataAt(2))
        


