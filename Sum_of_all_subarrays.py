'''Given an array of integers of size N, print the sum of sum of all subarrays.

Input Format
First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - size of the array and second line contains the elements of the array.

Output Format
For each test case, print the sum of sum of all subarrays, separated by newline.

Constraints
10 points
1 <= T <= 100
1 <= N <= 100

20 points
1 <= T <= 100
1 <= N <= 1000

70 points
1 <= T <= 1000
1 <= N <= 104

General Constraints
-106 <= arr[i] <= 106

Example
Input
3
3
3 4 5
2
1 2
3
1 -3 4

Output
40
6
3

Explanation

Test Case 1:
[3] + [3,4] + [3,4,5] + [4] + [4,5] + [5] = 40

Test Case 2:
[1] + [1,2] + [2] = 6

Test Case 3:
[1] + [1,-3] + [1,-3,4] + [-3] + [-3,4] + [4] = 3'''

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum_s = 0
    for i in range(1,n+1):
        sum_s += i*(n+1-i)*a[i-1]
        
    print(sum_s)
