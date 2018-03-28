

def ReverseArray(arr):
    b=arr[::-1]
    return b


if  __name__ =='__main__':
    print("Enter the number of elemnets")
    arr_count=int(input())

    print("enter elements of array\n")
    arr=list(map(int,input().rstrip().split()))
    print("array entered by you\n")
    print([int(i) for i in arr])
    res=ReverseArray(arr)
    print("reversed array: \n")
    print([int(x) for x in res])
