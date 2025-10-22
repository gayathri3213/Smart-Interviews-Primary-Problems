'''In a remote village, there is a new long marketplace with N stalls, all lined up along a straight path at positions x1, x2, x3,..., xN. A group of villagers, represented by C individuals, are highly protective of their personal space and tend to get into disputes when placed too close to one another. To maintain peace, the village leader wants to allocate the villagers to these stalls in a way that maximizes the minimum distance between any two of them.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains 2 space-separated integers - N and C. The second contains N integers, where ith integer denotes xi, the location of the ith stall.

Output Format
For each test case, print the largest minimum distance possible, separated by a new line.

Constraints
50 points
2 <= N <= 20
2 <= C <= N

100 points
2 <= N <= 104
2 <= C <= N

General Constraints
1 <= T <= 100
0 <= xi <= 106

Example
Input
1
5 3
1 2 9 8 4

Output
3

Explanation

Example 1:
The villagers should be placed at 1,4,9, which makes the minimum distance between them as 3. 
Any other combination will give a smaller minimum distance. '''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def isvalid(a,n,mid,k):
    relatives_placed=1
    prev=0
    for i in range(0,n):
        distance=a[i]-a[prev]
        if distance>=mid:
            relatives_placed+=1
            prev=i
    return relatives_placed>=k

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    lo,hi=0,a[n-1]-a[0]
    mid,ans=0,0
    while(lo<=hi):
        mid=(lo+hi)//2
        if isvalid(a,n,mid,k):
            ans=mid
            lo=mid+1
            #print(ans)
        else:
            hi=mid-1
    print(ans)
