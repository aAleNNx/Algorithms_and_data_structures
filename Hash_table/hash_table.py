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
            key = ord(key)
        return key % self.size
    
    def quadratic_probing(self, key, i):
        return (self.hash(key) + self.c1 * i + self.c2 * i**2) % self.size

    def search(self, key):
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None:
                return None
            if self.tab[idx].key == key:
                return self.tab[idx].value
        return None
    
    def insert(self, key, value):
        el = element(key, value)
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None:
                self.tab[idx] = el
                return
            elif self.tab[idx] is not None and self.tab[idx].key == key:
                self.tab[idx].value = value
                return
        raise Exception("Hash table is full")

    def remove(self, key):
        for i in range(self.size):
            idx = self.quadratic_probing(key, i)
            if self.tab[idx] is None:
                raise Exception("No element with this key")
            if self.tab[idx].key == key:
                self.tab[idx] = None
                return
            
    def __str__(self):
        ret = ""
        if not all(x is None for x in self.tab):
            for i in self.tab:
                ret += str(i)
                ret += ", "
            return "{" + ret[:-2] + "}"
        return ret


