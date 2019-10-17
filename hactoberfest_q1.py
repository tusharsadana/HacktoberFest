'''All submissions for this problem are available.Rishabh's friends like racing bicycles around the campus so he decides to buy a new bicycle and join them. But the bicycle of his choice does not come with a bell, so he has to buy one separately.He has very high awareness of safety, and decides to buy two bells, one for each hand.The store sells three kinds of bells for the price of a, b and c coins, respectively. Find the minimum total price of two different bells.

Input:
The first line of each test contains three integers a,b,c.
Output:
Print the minimum total price of two different bells.

Constraints
2≤a,b,c≤10000
a,b and c are integers.

Sample Input 1:
    700 600 780
Sample Output 1:
    1300'''


a,b,c=map(int, input().split())
list=[a,b,c]
mi1=min(list)
list.remove(mi1)
mi2=min(list)
sum=mi2+mi1
print(sum)
