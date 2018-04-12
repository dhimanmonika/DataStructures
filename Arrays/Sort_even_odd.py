l=[1,2,4,6,7,8,9]
m=[None]*len(l)

l.sort()
start=0
end = len(l)-1

for i in l:
    if i%2==0:
        m[start]=i
        start=start+1
    else:
        m[end]=i
        end=end-1

print(l,"\n",m)