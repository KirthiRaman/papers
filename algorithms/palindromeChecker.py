import sys
import deque

def palchecker(aString):
    chardeque = deque.Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


def main(argv):
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))

if __name__ == "__main__":
    main(sys.argv[1:])
