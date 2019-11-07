test=int(input())
for i in range(test):
    seq_len=int(input())
    list1 = list(map(int, input().split()))
    while True:
        least=min(list1)
        highest=max(list1)
        if least==highest:
            break
        temp = highest-least
        list1.remove(highest)
        list1.append(temp)
    print(list1[0])


