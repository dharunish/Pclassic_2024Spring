n = int(input())
for i in range(n):
    ns = int(input())
    sc = [int(i) for i in input().split()]
    test = []
    sp = [int(i) for i in input().split()]

    
    for i in range(len(sc)):
        try:
            if sp[i+1] > sp[i]:
                test.append(sc[:sc[i]])
        except IndexError:
            break
    print(len(test)+1)

