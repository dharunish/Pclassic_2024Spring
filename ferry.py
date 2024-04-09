p = int(input())
t = int(input())
d = [int(i) for i in input().split()]
d.sort()
c = int(input())
timef = int(input())
timep = int(input())
total = 0

if p > c:
    for i in range(p-c):
        total += timep * d[-i]
        d.pop(-i)
for des in d:
    total += des * timef
print(total)
