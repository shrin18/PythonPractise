class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    q = Queue()
    while True:
        print('enqueue <value>')
        print('dequeue <value>')
        print('quit')

        do = input('what would you like to do').split()

        operation = do[0].strip().lower
        
        