import sys

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.insert(0,item)

     def pop(self):
         return self.items.pop(0)

     def peek(self):
         return self.items[0]

     def size(self):
         return len(self.items)

def main(argv):
     s=Stack()

     print(s.isEmpty())
     s.push(4)
     s.push('algorithms')
     print(s.peek())
     s.push(True)
     print(s.size())
     print(s.isEmpty())
     s.push(9.82)
     print(s.pop())
     print(s.pop())
     print(s.size())

if __name__ == "__main__":
    main(sys.argv[1:])
