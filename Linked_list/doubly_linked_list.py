class node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        self.tail = None
        self.head = None

    def add(self, data):
        new_first = node(data, self.head, None)
        self.head = new_first
        if self.tail is None:
            self.tail = new_first
            return
        (self.head.next).prev = new_first

    def append(self, data):
        new_last = node(data, None, self.tail)
        self.tail = new_last
        if self.head is None:
            self.head = new_last
            return
        (self.tail.prev).next = new_last

    def remove(self):
        if self.head == None:
            return
        if self.tail is self.head:
            self.tail = None
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_end(self):
        if self.tail == None:
            return
        if self.tail is self.head:
            self.tail = None
            self.head = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        curr = self.head
        i = 0
        while curr != None:
            i += 1
            curr = curr.next
        return i

    def get(self):
        if self.head == None:
            return None
        return self.head.data
    
    def get_last(self):
        if self.tail == None:
            return None
        return self.tail.data
    
    def print_list(self):
        curr = self.head
        if curr == None:
            print('list is empty')
            return
        while curr.next != None:
            print(f'-> {curr.data}')
            curr = curr.next
        print(f'-> {curr.data}')

    def print_back(self):
        curr = self.tail
        if curr == None:
            print('list is empty')
            return
        while curr.prev != None:
            print(f'-> {curr.data}')
            curr = curr.prev
        print(f'-> {curr.data}')
