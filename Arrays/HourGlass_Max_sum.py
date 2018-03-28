def array2D(arr):
    max_sum = -999
    for i in range(4):
        for j in range(4):
            s = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                arr[i + 2][j + 2]
            if max_sum < s:
                max_sum = s
    return max_sum


if __name__ == '__main__':

    arr = []
    print("enter 6*6 array\n")
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)
    print("max sum :",result)