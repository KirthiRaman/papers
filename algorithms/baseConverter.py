import sys
import stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = stack.Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


def main(argv):
   print(baseConverter(175,2))
   print(baseConverter(493,16))

if __name__ == "__main__":
    main(sys.argv[1:])
