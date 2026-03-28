class queue_cir:
    def __init__(self, size = 5):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.write_idx = 0
        self.read_idx = 0

    def is_empty(self):
        return self.write_idx == self.read_idx
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.read_idx]
        
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[self.read_idx]
        self.queue[self.read_idx] = None
        self.read_idx = (self.read_idx + 1) % self.size
        return value
    
    def enqueue(self, data):
        self.queue[self.write_idx] = data
        self.write_idx = (self.write_idx + 1) % self.size
        if self.write_idx == self.read_idx:
            self.queue = self.queue[:self.read_idx] + [None for i in range(self.size)] + self.queue[self.read_idx:]
            self.size *= 2
            self.read_idx = (self.read_idx + int(self.size/2)) % self.size

    def __str__(self):
        result = "["
        idx = self.read_idx
        while idx != self.write_idx:
            result += str(self.queue[idx])
            result += ", "
            idx = (idx + 1) % self.size 
        result = result.rstrip(", ") + "]"
        return result
    
