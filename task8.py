def canI (m, n, k):
    if (k % n == 0) or (k % m == 0):
        print("yes")
    else:
        print("no")


n = int(input())
m = int(input())
k = int(input())
canI(n, m, k)