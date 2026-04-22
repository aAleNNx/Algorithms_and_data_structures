import random
import time
import copy
class node:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority
    
    def __repr__(self):
        return f"{self.__priority} : {self.__data}"
    
class Heap:
    def __init__(self, tab = None):
        self.tab = tab if tab is not None else []
        self.size = len(self.tab)
        self.reheap()

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        a = self.tab[0]
        self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
        self.size -= 1
        self.repair(0)
        return a
    
    def repair(self, idx):
        curr = idx
        while True:
            l = self.left(curr)
            r = self.right(curr)
            largest = curr

            if l is not None and l < self.size and self.tab[l] > self.tab[largest]:
                largest = l

            if r is not None and r < self.size and self.tab[r] > self.tab[largest]:
                largest = r

            if largest == curr:
                break

            self.tab[curr], self.tab[largest] = self.tab[largest], self.tab[curr]
            curr = largest

    def reheap(self):
        if self.size == 0:
            return
        for i in range(self.parent(self.size - 1), -1, -1):
            self.repair(i)

    def enqueue(self, obj):
        self.size += 1
        if self.size > len(self.tab):
            self.tab.append(obj)
        else:
            self.tab[self.size - 1] = obj
        curr = self.size - 1
        while self.parent(curr) is not None:
            if self.tab[self.parent(curr)] < self.tab[curr]:
                self.tab[curr], self.tab[self.parent(curr)] = self.tab[self.parent(curr)], self.tab[curr]
                curr = self.parent(curr)
            else:
                return          

    def left(self, idx):
        if (2*idx + 1) >= self.size:
            return None
        return (2*idx + 1)
    

    def right(self, idx):
        if (2*idx + 2) >= self.size:
            return None
        return (2*idx + 2)

    def parent(self, idx):
        if idx == 0:
            return None
        return (idx - 1) // 2

    def print_tree(self, idx, lvl):
        if idx is not None and idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)  

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end = ' ')
        print( '}')

def swap_sort(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range (i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        
def shift_sort(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range (i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        min_val = tab[min_index]
        tab.pop(min_index)
        tab.insert(i, min_val)
        
def heap_sort(tab):
    heap = Heap(tab)
    for i in range(heap.size):
        heap.dequeue()
    return heap.tab


def test1_1():
    print("\n___TEST 1___HEAPSORT___\n")
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'),
            (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

    elems = [node(v, k) for k, v in data]

    heap = Heap(elems)

    heap.print_tab()
    heap.print_tree(0, 0)

    n = heap.size
    first_tab = []
    for i, j in data:
        first_tab.append(f'{i}:{j}')

    print(first_tab)
    for i in range(n):
        heap.dequeue()
    print(heap.tab)
    print("NIESTABILNE")
    
    print("\n___TEST 2___SWAP___\n")

    elems2 = [node(v, k) for k, v in data]

    swap_sort(elems2)

    print(first_tab)
    print(elems2)
    print("NIESTABILNE")

    print("\n___TEST 3___SHIFT___\n")

    elems3 = [node(v, k) for k, v in data]

    shift_sort(elems3)

    print(first_tab)
    print(elems3)
    print("STABILNE")


def test1_2():
    print("\n___TEST 1___HEAPSORT___\n")
    data = [13, 5, 7, 2, 5, 1, 7, 5, 1, 2, 11, 2, 3, 4, 6, 8, 9, 10, 12, 14]

    elems = data.copy()

    heap = Heap(elems)

    heap.print_tab()
    heap.print_tree(0, 0)

    n = heap.size

    print(data)
    for i in range(n):
        heap.dequeue()  
    print(heap.tab)
    print("NIESTABILNE")
    
    print("\n___TEST 2___SWAP___\n")

    elems2 = data.copy()

    swap_sort(elems2)

    print(data)
    print(elems2)
    print("NIESTABILNE")

    print("\n___TEST 3___SHIFT___\n")

    elems3 = data.copy()

    shift_sort(elems3)

    print(data)
    print(elems3)
    print("STABILNE")

user_input = input("Wybierz test (1_1 lub 1_2): ")
if user_input == '1_1':
    test1_1()
elif user_input == '1_2':
    test1_2()
else:
    print("Nieprawidłowy wybór. Wybierz 1_1 lub 1_2.")

def test2_1(tab):
    start_time = time.perf_counter()
    tab = heap_sort(tab)
    end_time = time.perf_counter()
    return end_time - start_time

def test2_2(tab):
    start_time = time.perf_counter()
    tab = swap_sort(tab)
    end_time = time.perf_counter()
    return end_time - start_time

def test2_3(tab):
    start_time = time.perf_counter()
    tab = shift_sort(tab)
    end_time = time.perf_counter()
    return end_time - start_time

tab = [int(random.random() * 100) for _ in range(10000)]
tab1 = copy.deepcopy(tab)
tab2 = copy.deepcopy(tab)
tab3 = copy.deepcopy(tab)

print("Czas obliczeń heap_sort:", "{:.7f}".format(test2_1(tab1)), "sekund")
print("Czas obliczeń swap_sort:", "{:.7f}".format(test2_2(tab2)), "sekund")
print("Czas obliczeń shift_sort:", "{:.7f}".format(test2_3(tab3)), "sekund")