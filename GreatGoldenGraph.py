s = input()
n = int(input())
check = 0
while True:
    if len(s) > n:
        break
    n = n - len(s)
print(s[n-1])