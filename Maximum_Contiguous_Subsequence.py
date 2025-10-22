'''Given an array, find the length of the longest subsequence whose elements can be re-arranged in a strictly increasing contiguous order. The difference between 2 adjacent elements in the subsequence, after re-arrangement, should be exactly 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - size of the array. The next line contains N integers - the elements of the array.

Output Format
For each test case, print the length of the longest subsequence, separated by a new line.

Constraints
1 <= T <= 1000
1 <= N <= 10000
-100000 <= ar[i] <= 100000

Example
Input
3
8
21 -22 -22 5 -31 -24 5 -23
10
18 -33 31 33 30 -14 32 30 16 17
6
6 3 8 5 2 5

Output
3
4
2

Explanation

Test Case-1:
Subsequence is: -22, -24, -23.

Test Case-2: 
Subsequence is: 31, 33, 30, 32.

Test Case-3: 
Subsequence is: 6, 5 or 3, 2.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    
    
    max_len=0
    current=1
    for i in range(1,n):
        #current = 1
        if abs(a[i] - a[i-1])==1:
            current+=1
        elif abs(a[i] - a[i-1])==0:
            continue
        else:
            max_len=max(max_len,current)
            current=1
    max_len=max(max_len,current)
    print(max_len)
