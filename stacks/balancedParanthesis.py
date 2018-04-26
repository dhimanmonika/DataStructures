import sys
left='({['
right=')}]'
closes={a:b for a,b in zip(right,left)}

def isBalanced(s):
    # Complete this function
    stack=[]
    for c in s:
        if c in left:
            stack.append(c)
        elif c in right:
            if not stack or stack.pop()!=closes[c]:
                return "NO"
    if not stack:
        return "YES"
    else :
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
