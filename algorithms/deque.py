import sys

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def main(argv):
     d=Deque()

     print(d.isEmpty())
     d.addRear(4)
     d.addRear('Math')
     d.addFront('Computer Science')
     d.addFront(True)
     print(d.size())
     print(d.isEmpty())
     d.addRear(8.4)
     print(d.removeRear())
     print(d.removeFront())

if __name__ == "__main__":
    main(sys.argv[1:])
