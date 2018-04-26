

"""INPUT FORMAT

5 3 4    NO OF ELEMENTS OF EACH STACK
3 2 1 1 1   ELEMENTS OF STACK ONE
4 3 2       ELEMENTS OF STACK TWO
1 1 4 1     ELEMENTS OF STACK THREE

"""

def equalStacks(h1, h2, h3):

    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    while (s1!=s2 and s1!=s3 and s2!=s3) :
            if s1 < s2 and s1 < s3:
                h2.pop(0)
                h3.pop(0)

            elif s3<s1 and s3<s2:
                h1.pop(0)
                h2.pop(0)

            elif s2 < s1 and s2 < s3:
                h1.pop(0)
                h3.pop(0)

            elif s1 == s2 :
                if s1 < s3:
                    h3.pop(0)
                else:
                    h1.pop(0)
                    h2.pop(0)
            elif s1 == s3 :
                if s1 < s2:
                    h2.pop(0)
                else:
                    h1.pop(0)
                    h3.pop(0)
            elif s2 == s3 :
                if s2 < s1:
                    h1.pop(0)
                else:
                    h2.pop(0)
                    h3.pop(0)
            s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    return s1



if __name__ == '__main__':
    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    #print(str(result) + '\n')
    print(result)

