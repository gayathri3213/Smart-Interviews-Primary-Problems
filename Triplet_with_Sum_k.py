'''You are given an integer array and a positive integer K. You have to tell if there exists i,j,k in the given array such that ar[i]+ar[j]+ar[k]=K, i≠j≠k.

Input Format
The first line of input contains T - the number of test cases. Its followed by 2T lines, the first line contains N and K - the size of the array and the number K. The second line contains the elements of the array.

Output Format
For each test case, print "true" if the arrays contains such elements, "false" otherwise, separated by new line.

Constraints
30 points
1 <= T <= 100
3 <= N <= 100

70 points
1 <= T <= 100
3 <= N <= 1000

General Constraints
-105 <= A[i] <= 105
0 <= K <= 105

Example
Input
3
5 60
1 20 40 100 80
12 54
12 45 52 65 21 645 234 -100 14 575 -80 112
3 15
5 5 5

Output
false
true
true'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    array=list(map(int,input().split()))

    count=0
    array.sort()

    for i in range(n):
        j,l=i+1,n-1

        if array[i]==array[i-1] and i>0:
            continue
        
        while j<l:
            s=array[i] + array[j] + array[l]
            if s==k:
                count+=1
                break
            elif s>k:
                l-=1
            elif s<k:
                j+=1

    if count==0:
        print('false')
    else:
        print('true')
