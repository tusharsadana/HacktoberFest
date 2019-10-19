a,b,c=map(int, input().split())
list=[a,b,c]
mi1=min(list)
list.remove(mi1)
mi2=min(list)
sum=mi2+mi1
print(sum)