



def majorityElement(a):
    max=0
    for item in a:
        c=a.count(item)
        if c>max:
            max=c
            maj_elem=item
    return maj_elem



arr=[1,2,3,5,2,16,2]
res=majorityElement(arr)
print("majority elemnt of array is ",res)