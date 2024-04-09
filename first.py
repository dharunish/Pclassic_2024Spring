
def findOdd(bees):
    check = 0
    for i in bees:
        if i % 2 != 0:
            check = 1
            print(i)
    if check == 0:
        print(0)

    
    
ntest = int(input())
for t in range(ntest):
    nbees = int(input())
    bees = [int(i) for i in input().split()]
    findOdd(bees)


    