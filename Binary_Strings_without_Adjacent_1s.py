'''Find the number of binary strings of length N, such that there are no adjacent 1s in that string.

Input Format
The first line of input contains T - number of test cases. It is followed by T lines, each line contains N - length of the binary string.

Output Format
For each test case, print the number of binary strings of length N, separated by new line. Since the answer can be very large, print answer % 1000000007 [1e9+7].

Constraints
1 <= T <= 105
1 <= N <= 105

Example
Input
5
3
11
7
5
500

Output
5
233
34
13
73724597

Explanation

Example 1:
You can construct the following binary strings of length 3 with no adjacent 1s:
000, 001, 010, 100, 10'''

import sys
sys.setrecursionlimit(10**7)
dp=[-1]*(10**5+1)
MOD=int(1e9+7)
dp[0]=0
dp[1]=2
dp[2]=3

def solve(n):
    if dp[n]!=-1:
        return dp[n]
    if n==1 or n==2 or n==0:
        return dp[n]
    else:
        dp[n-1]=solve(n-1)
        dp[n-2]=solve(n-2)
        dp[n]=(dp[n-1]%MOD + dp[n-2]%MOD) %MOD
        return dp[n]
for _ in range(int(input())):
    n=int(input())
    print(solve(n))
