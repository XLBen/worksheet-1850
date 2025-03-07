# for loop sum

import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} num1 num2 ...")
        return
    
    # sum
    total = sum(int(num) for num in sys.argv[1:])

    # print
    print(f"Sum: {total}")
