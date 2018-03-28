
import os
import sys


if __name__ == '__main__':
    print("Enter the number of elements and shifting number of  times \n")
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    print("enter array elements\n")
    a = list(map(int, input().rstrip().split()))

    b = a[d:]
    b = b + (a[0:d])
    print("array after left shift\n")
    print(" ".join(map(str,b)))