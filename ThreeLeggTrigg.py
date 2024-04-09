import math

l = [int(i) for i in input().split()]
if l[0] - l[1] == 0:
    print(0)
elif l[1] >= (l[0] / 2):
    print(1)
else:
    print(math.floor(l[0]/(l[1]+1)))





    


'''
e = l[0]
elist = []
for i in range(e):
    elist.append(i)

w = l[1]
if e - w == 0:
    print(0)
else:
    d = round(e/(w+1))
    test = (elist[::d])
print(max(test))
'''

    