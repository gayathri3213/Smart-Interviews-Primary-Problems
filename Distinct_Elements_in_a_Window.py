'''
Given an array of integers and a window size K, find the number of distinct elements in every window of size K of the given array.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains the N-size of the array and the K-size of the window. The second line contains N integers - elements of the array.

Output Format
For each test case, print the number of distinct elements in every window of size K, separated by a new line.

Constraints
30 points
1 <= N <= 100
1 <= K <= N

70 points
1 <= N <= 10000
1 <= K <= N

General Constraints
1 <= T <= 1000
-100 <= ar[i] <= 100

Example
Input
3
5 3
-2 -4 -2 4 -2
10 7
3 -4 -3 -4 -2 0 2 -2 6 0
17 13
-5 -1 4 8 -5 -3 -4 7 4 -4 0 8 0 -2 3 2 5

Output
2 3 2
6 5 6 5
8 9 9 10 11'''

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    my_dict = {}

    for i in range(0,k):
        if a[i] in my_dict:
            my_dict[a[i]] = my_dict[a[i]] + 1
        else:
            my_dict[a[i]] = 1
    print(len(my_dict),end=' ')

    for i in range(k,n):
        outgoing = a[i-k]
        incoming = a[i]

        my_dict[outgoing]-=1
        if my_dict[outgoing] == 0:
            del my_dict[outgoing]

        if incoming in my_dict:
            my_dict[incoming]+=1
        else:
            my_dict[incoming] = 1
        
        print(len(my_dict),end=' ')
    print()
