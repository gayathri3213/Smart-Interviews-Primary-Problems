'''You are given an array of size N containing unique integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.
A contiguous sequence means that the difference of adjacent elements should be 1.

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
5
1 3 2 6 5
9
0 8 6 5 7 10 3 2 1

Output
3
4

Explanation

Test-Case 1
The largest subarray that can be rearranged to form a contiguous sequence is [1, 3, 2] 
which can be rearranged to form [1, 2, 3].

Test-Case 2
The largest subarray that can be rearranged to form a contiguous sequence is [8, 6, 5, 7] 
which can be rearranged to form [5, 6, 7, 8].'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    max_len = 1

    for i in range(n):
        max_ele,min_ele=a[i],a[i]
        for j in range(i,n):
            if a[j] > max_ele:
                max_ele = a[j]
            if a[j] < min_ele:
                min_ele = a[j]
            
            range_value = max_ele - min_ele + 1
            length = j-i+1

            #print(a[i:j+1],max_ele,max_len,range_value,length)

            if range_value == length:
                max_len = max(max_len,length)
    print(max_len)
