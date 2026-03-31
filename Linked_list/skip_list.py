import random

def randomLevel(p, maxLevel):
    lvl = 1
    while random.random() < p and lvl < maxLevel:
        lvl += 1
    return lvl


class Node:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.level = level
        self.tab = [None] * level


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Node(None, None, max_level)

    def search(self, key):
        current = self.head
        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] and current.tab[lvl].key < key:
                current = current.tab[lvl]

        current = current.tab[0]

        if current and current.key == key:
            return current.data
        return None

    def insert(self, key, data):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current and current.key == key:
            current.data = data
            return

        lvl = randomLevel(0.5, self.max_level)
        new_node = Node(key, data, lvl)

        for i in range(lvl):
            new_node.tab[i] = update[i].tab[i]
            update[i].tab[i] = new_node

    def remove(self, key):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current and current.key == key:
            for i in range(current.level):
                if update[i].tab[i] != current:
                    break
                update[i].tab[i] = current.tab[i]

    def __str__(self):
        result = []
        node = self.head.tab[0]
        while node:
            result.append(f"({node.key}:{node.data})")
            node = node.tab[0]
        return "[" + ", ".join(result) + "]"

    def displayList_(self):
        node = self.head.tab[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while idx < len(keys) and node.key > keys[idx]:
                    print("     ", end="")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()

if __name__ == "__main__":
    random.seed(42)

    print("=== TEST 1 (1 -> 15) ===")
    sl = SkipList(5)

    for i in range(1, 16):
        sl.insert(i, chr(64 + i))

    sl.displayList_()

    print("Search 2:", sl.search(2))

    sl.insert(2, 'Z')
    print("Search 2:", sl.search(2))

    sl.remove(5)
    sl.remove(6)
    sl.remove(7)

    print("Po usunięciu:", sl)

    sl.insert(6, 'W')
    print("Po dodaniu 6:", sl)

    print("\n=== TEST 2 (15 -> 1) ===")
    sl2 = SkipList(5)

    for i in range(15, 0, -1):
        sl2.insert(i, chr(64 + i))

    sl2.displayList_()

    print("Search 2:", sl2.search(2))

    sl2.insert(2, 'Z')
    print("Search 2:", sl2.search(2))

    sl2.remove(5)
    sl2.remove(6)
    sl2.remove(7)

    print("Po usunięciu:", sl2)

    sl2.insert(6, 'W')
    print("Po dodaniu 6:", sl2)