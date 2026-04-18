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
    def __init__(self):
        self.tab = []
        self.size = 0

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

kol = Heap()
lista = [7, 5, 1, 2, 5, 3, 4, 8, 9]
napis = "GRYMOTYLA"
for i in range(len(lista)):
    kol.enqueue(node(napis[i], lista[i]))

kol.print_tree(0, 0)
print("")
kol.print_tab()

a = kol.dequeue()
print(kol.peek())
kol.print_tab()
print(f'Pierwsza zapamiętana: {a}')
for i in range(kol.size):
    print(kol.dequeue())
    
kol.print_tab()
