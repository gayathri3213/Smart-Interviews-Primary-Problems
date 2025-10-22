'''Given an array of integers of size N, count the number of subarrays of given array which are non-decreasing.

Input Format
First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - size of the array and second line contains the elements of the array.

Output Format
For each test case, print the count of number of subarrays which are non-decreasing, separated by newline.

Constraints
10 points
1 <= T <= 100
1 <= N <= 102

20 points
1 <= T <= 100
1 <= N <= 103

70 points
1 <= T <= 100
1 <= N <= 105

General Constraints
1 <= arr[i] <= 109

Example
Input
3
6
2 3 1 4 6 6
1
5
3
1 3 2

Output
13
1
4

Explanation

Test Case 1:
All the valid subarrays are: [2], [2,3], [3], [1], [1,4], [1,4,6], [1,4,6,6], 
[4], [4,6], [4,6,6], [6], [6,6], [6]

Test Case 2:
All the valid subarrays are: [5]

Test Case 3:
All the valid subarrays are: [1], [1,3], [3], [2]'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans_c=0
    len_s=1
    i=0
    while i<len(a)-1:
        if a[i]<=a[i+1]:
            len_s+=1
            #print(a[i],a[i+1],len_s)
            i+=1
        else:
            ans_c = ans_c + (len_s*(len_s+1))//2
            #print(i,ans_c,len_s)
            len_s=1
            i+=1
    ans_c = ans_c + (len_s*(len_s+1))//2
    #print(i,ans_c)   
    print(ans_c)
