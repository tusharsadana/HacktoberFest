'''
Akash, Shikhar and Kalpaj are at a pub and drinking a magical potion. All three of them are at queue and there are no other people in the queue. The first person in the queue Akash drinks the first magical potion and doubles! Then both of them go and stand at the back of the queue. Then Shikhar, who is next in the queue, drinks the second magical potion and goes and stands at the end of the queue behind Akash. Now, the queue looks like this: Kalpaj, Akash, Akash, Shikhar, Shikhar
The same process continues and after Kalpaj drinks the potion, the people behind him will continue the process. Find the person who will drink the Nth Magical Potion.

Input Format

First line will contain T, the number of Test Cases.
For each Test Case, there will be a single integer N, for which you have to find the person who will drink the Nth Magical potion.
Constraints

1 ≤ T ≤ 5
1 ≤ N ≤ 10000
Output Format

For each Test Case, print on a single line the name of the person who will drink the Nth Magical potion.
Please take care of the spelling and print them as "Akash", "Shikhar" & "Kalpaj", without quotes.
Sample Input 0

3
1
2
8
Sample Output 0

Akash
Shikhar
Kalpaj
'''

test = int(input('enter the test nos:'))
for i in range(test):
    queue = ['Akash', 'Shikhar', 'Kalpaj']
    drank = 'na'
    while True:
        portion_no = float(input('Enter the portion no:'))
        for l in range(0,int(portion_no)):
            temp = queue[0]
            drank=temp
            queue.pop(0)
            queue.append(temp)
            queue.append(temp)
        break
    print(drank)
