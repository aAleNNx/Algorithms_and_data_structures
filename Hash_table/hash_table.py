DELETED = object()

class element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'{self.key}:{self.value}'

class hash_table:
    def __init__(self, size = 5, c1 = 1, c2 = 0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for _ in range (size)]

    def hash(self, key: str|int):
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return key % self.size
    
    def quadratic_probing(self, key, i):
        return (self.hash(key) + self.c1 * i + self.c2 * i**2) % self.size

    def search(self, key):
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None:
                return None
            if self.tab[idx] is not DELETED and self.tab[idx].key == key:
                return self.tab[idx].value
        return None
    
    def insert(self, key, value):
        el = element(key, value)
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None or self.tab[idx] is DELETED:
                self.tab[idx] = el
                return
            elif self.tab[idx].key == key:
                self.tab[idx].value = value
                return
        print("Hash table is full")
        return

    def remove(self, key):
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None:
                print("Element not found")
                return
            if self.tab[idx].key == key and self.tab[idx] is not DELETED:
                self.tab[idx] = DELETED
                return
            
    def __str__(self):
        ret = ""
        if not all(x is None for x in self.tab):
            for i in self.tab:
                if i is not None and i is not DELETED:
                    ret += str(i)
                    ret += ", "
                if i is DELETED or i is None:
                    ret += "None, "
            return "{" + ret[:-2] + "}"
        return ret


def test_1(size, c1 = 1, c2 = 0):
    ht = hash_table(size, c1, c2)
    data = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (18, 'F'), (31, 'G'), (8, 'H'), (9, 'I'), (10, 'J'), (11, 'K'), (12, 'L'), (13, 'M'), (14, 'N'), (15, 'O')]
    for key, value in data:
        ht.insert(key, value)
    print(ht)
    print(ht.search(5))
    print(ht.search(14))
    ht.insert(5, 'Z')
    print(ht)
    ht.remove(5)
    print(ht)
    print(ht.search(31))
    ht.insert("test", 'W')
    print(ht)

def test_2(size, c1=1, c2=0):
    ht = hash_table(size, c1, c2)

    data = [(13*i, chr(ord('A') + i - 1)) for i in range(1, size+1)]

    for key, value in data:
        ht.insert(key, value)

    print(ht)

def main():
    print("\n=== Test 1 ===")
    test_1(13, 1, 0)
    
    print("\n=== Liniowe ===")
    test_2(13, 1, 0)

    print("\n=== Kwadratowe ===")
    test_2(13, 0, 1)

    print("\n=== Test 1 + kwadratowe ===")
    test_1(13, 0, 1)


if __name__ == "__main__":    
    main()