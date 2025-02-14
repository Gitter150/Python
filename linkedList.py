class LinkedList:
    class Node:
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None
    def __init__(self):
        self.head = None
        self.tail = None
    