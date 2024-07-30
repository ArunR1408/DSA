def lbs(arr):
    n = len(arr)
    lis = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    lds = [1 for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    maximum = lis[0] + lds[0] - 1
    for i in range(1, n):
        maximum = max((lis[i] + lds[i] - 1), maximum)
    
    return maximum

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(lbs(arr))

if __name__ == "__main__":
    main()