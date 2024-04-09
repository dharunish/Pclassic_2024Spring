n = int(input())
c = [int(i) for i in input().split()]
min = min(c)
max = max(c)
sum = 0
for i in c:
    if i == min:
        sum += abs(max - i)
    elif i == max:
        sum += abs(i - min)
    else:
        t1 = abs(i - min)
        t2 = abs(i - max)
        if t1 > t2:
            sum += t1
        else:
            sum += t2
print(sum)
