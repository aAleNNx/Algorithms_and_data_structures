CAPACITY = 6


class Node:
    def __init__(self):
        self.node_arr = [None] * CAPACITY
        self.count = 0
        self.next = None

    def insert_at(self, idx, data):
        if self.count == CAPACITY:
            raise Exception("Node is full")

        if idx < 0:
            raise ValueError

        if idx >= self.count:
            self.node_arr[self.count] = data
        else:
            for i in range(self.count, idx, -1):
                self.node_arr[i] = self.node_arr[i - 1]
            self.node_arr[idx] = data

        self.count += 1

    def delete_at(self, idx):
        if idx < 0 or idx >= self.count:
            raise IndexError

        for i in range(idx, self.count - 1):
            self.node_arr[i] = self.node_arr[i + 1]

        self.node_arr[self.count - 1] = None
        self.count -= 1


class UnrolledLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError

        current = self.head

        while current:
            if idx < current.count:
                return current.node_arr[idx]
            idx -= current.count
            current = current.next

        raise IndexError

    def insert(self, idx, data):
        if idx < 0:
            raise IndexError

        if self.head is None:
            self.head = Node()
            self.head.insert_at(0, data)
            self.size += 1
            return

        if idx > self.size:
            idx = self.size

        current = self.head
        prev = None

        while current:
            if idx <= current.count:
                break
            idx -= current.count
            prev = current
            current = current.next

        if current is None:
            current = prev

        if current.count < CAPACITY:
            current.insert_at(idx, data)
        else:
            new_node = Node()
            mid = CAPACITY // 2

            for i in range(mid, CAPACITY):
                new_node.node_arr[i - mid] = current.node_arr[i]
                new_node.count += 1

            current.count = mid

            new_node.next = current.next
            current.next = new_node

            if idx <= mid:
                current.insert_at(idx, data)
            else:
                new_node.insert_at(idx - mid, data)

        self.size += 1

    def delete(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError

        current = self.head
        prev = None

        while current:
            if idx < current.count:
                break
            idx -= current.count
            prev = current
            current = current.next

        current.delete_at(idx)

        if current.next is None:
            if current.count == 0 and prev:
                prev.next = None
            self.size -= 1
            return

        if current.count < CAPACITY // 2:
            next_node = current.next

            if next_node.count > CAPACITY // 2:
                current.node_arr[current.count] = next_node.node_arr[0]
                current.count += 1
                next_node.delete_at(0)
            else:
                for i in range(next_node.count):
                    current.node_arr[current.count + i] = next_node.node_arr[i]

                current.count += next_node.count
                current.next = next_node.next

        self.size -= 1
    
    def print_list(self):
        current = self.head
        while current:
            print(current.node_arr[:current.count], end=" -> ")
            current = current.next
        print("None")

ull = UnrolledLinkedList()

for i in range(1, 10):
    ull.insert(i - 1, i)

print(ull.get(4))

ull.insert(1, 10)
ull.insert(8, 11)

ull.print_list()

ull.delete(1)
ull.delete(2)

ull.print_list()