class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        new_first = node(data, self.head)
        self.head = new_first 

    def append(self, data):
        curr = self.head
        while curr != None:
            if curr.next == None:
                curr.next = node(data, None)
                return
            curr = curr.next
        self.head = node(data, None)

    def remove(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_end(self):
        curr = self.head
        if curr is None:
            return
        if curr.next is None:
            self.head = None
            return
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def lenght(self):
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
    
    def print(self):
        curr = self.head
        if curr == None:
            print('list is empty')
            return
        while curr.next != None:
            print(f'-> {curr.data}')
            curr = curr.next
        print(f'-> {curr.data}')







