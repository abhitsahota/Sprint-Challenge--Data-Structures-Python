class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.pointer = 0
        self.storage = []

    def append(self, item):
        if self.size < self.capacity:
            self.size +=1
            self.storage.append(item)
        if self.pointer < self.capacity:
            del self.storage[self.pointer]
            self.storage.insert(self.pointer, item)
        else:
            self.pointer = 0
            del self.storage[self.pointer]
            self.storage.insert(self.pointer, item)
        self.pointer +=1
        return self.storage

    def get(self):
        for i in range(0, len(self.storage)):
            if self.storage[i] is None:
                del self.storage[i]
        return self.storage