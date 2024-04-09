s = [int(i) for i in input().split()]
while True:
    m = s[0]*s[1]
    if m - s[2] == 0:
        print('YES')
        break
    m = s[0]*s[2]
    if m - s[1] == 0:
        print('YES')
        break
    m = s[1]*s[2]
    if m - s[0] == 0:
        print('YES')
        break



    m = s[0] - s[1]
    if m*s[2] == 0:
        print('YES')
        break
    m = s[0] - s[2]
    if m*s[1] == 0:
        print('YES')
        break
    m = s[1] - s[0]
    if m*s[2] == 0:
        print('YES')
        break
    m = s[1] - s[2]
    if m*s[0] == 0:
        print('YES')
        break
    m = s[2] - s[0]
    if m*s[1] == 0:
        print('YES')
        break
    m = s[2] - s[1]
    if m*s[0] == 0:
        print('YES')
        break
    print('NO')
    break
