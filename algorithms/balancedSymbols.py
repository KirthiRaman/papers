import sys
import stack

def balancedSymbols(symbolString):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)



def main(argv):
    print(balancedSymbols('{{([][])}()}'))
    print(balancedSymbols('[{()]'))

if __name__ == "__main__":
    main(sys.argv[1:])
