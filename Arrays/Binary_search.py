def binary_search(arr,item,start,end):
    if start==end:
        return -1
    mid=round((end+start)/2)
    if arr[mid] < item:
       return binary_search(arr,item,mid+1,end)
    elif arr[mid] > item:
       return binary_search(arr,item,start,mid-1)
    elif arr[mid]==item:
       return mid




arr=[1,2,3,5,12,16]
print("enter number to search in array :")
try:
    num=int(input())
    res = binary_search(arr, num, 0, 6)
    if res < 0:
        print("NOT FOUND")
    else:
        print("present at position ", res + 1)
except:
    print("only integers allowed")


