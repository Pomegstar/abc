class queu:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        return self.items.append(item)
    def deque(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    