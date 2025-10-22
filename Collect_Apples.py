'''You are given a maze containing cells. Each cell has certain number of apples. You have to start from the top-left position and traverse all the way to the bottom-right position, collecting apples on your way. You can move only in right and downward direction, i.e., from any cell (i,j) you can only move right: (i,j+1) or down: (i+1,j). Find the maximum number of apples you can collect.

Input Format
The first line of input contains T - number of test cases. First line of each test case contains N and M - the size of the maze. It is followed by N lines, each containing M integers indicating the number of apples in the cell.

Output Format
For each test case, print the maximum number of apples you can collect, separated by new line.

Constraints
1 <= T <= 100
1 <= N,M <= 300
0 <= Aij <= 100

Example
Input
2
3 4
1 5 1 4
10 11 0 13
4 15 1 12
4 2
4 5
1 3
10 5
1 0

Output
50
20

Explanation

Example 1:
The path using which you can collect maximum apples is highlighted below:
1 5 1 4
10 11 0 13
4 15 1 12
Total Apples = 1 + 10 + 11 + 15 + 1 + 12 = 50

Example 2:
The path using which you can collect maximum apples is highlighted below:
4 5
1 3
10 5
1 0
Total Apples = 4 + 1 + 10 + 5 + 0 = 2'''

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    apples=[]
    for N in range(n):
        row=list(map(int,input().split()))
        apples.append(row)
    for i in range(1,m):
        apples[0][i]+=apples[0][i-1]
    for i in range(1,n):
        apples[i][0]+=apples[i-1][0]
    for i in range(1,n):
        for j in range(1,m):
            apples[i][j]=max(apples[i-1][j],apples[i][j-1])+apples[i][j]
    print(apples[n-1][m-1])
