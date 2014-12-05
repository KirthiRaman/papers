import sys
import stack

def parChecker(symbolString):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def main(argv):
     print(parChecker('((()))'))
     print(parChecker('(()'))

if __name__ == "__main__":
    main(sys.argv[1:])
