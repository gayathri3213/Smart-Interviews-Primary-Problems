'''You are given an array of size N containing integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.
A contiguous sequence means that the difference of adjacent elements should be 0 or 1.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.

Output Format
For each test case, print the size of the largest subarray that can be rearranged to form a contiguous sequence, on a new line.

Constraints
30 points
1 <= T <= 100
4 <= N <= 100

70 points
1 <= T <= 100
4 <= N <= 1000

General Constraints
0 <= A[i] <= 105

Example
Input
2
6
5 2 3 3 1 1
9
8 8 6 7 3 5 7 4 1

Output
5
8

Explanation

Test-Case 1
The largest subarray which can be rearranged to form a contiguous sequence is [2, 3, 3, 1, 1] 
which can be rearranged to form [1, 1, 2, 3, 3].

Test-Case 2
The largest subarray which can be rearranged to form a contiguous sequence is 
[8, 8, 6, 7, 3, 5, 7, 4] which can be rearranged to form [3, 4, 5, 6, 7, 7, 8, 8].'''

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    set_a=set()
    max_len=1

    for i in range(n):
        max_ele,min_ele=a[i],a[i]
        set_a.clear()
        for j in range(i,n):
            set_a.add(a[j])
            if a[j]>max_ele:
                max_ele=a[j]
            if a[j]<min_ele:
                min_ele=a[j]
            range_value = max_ele - min_ele + 1
            length = j-i+1
            if range_value==len(set_a):
                max_len = max(length,max_len)
    print(max_len)
