a=int(input())
for i in range(a):
    str = input()
    tempstr = list(str)
    count1 = 0
    for i in range(len(tempstr)):
        temp = tempstr[i]
        count = 0
        for j in range(len(tempstr)):
            if tempstr[j]==temp:
                count+=1
        if count>1:
            break
    if count > 1:
        print('no')
    elif count == 1:
        print('yes')