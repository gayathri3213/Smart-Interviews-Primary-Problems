'''Understand the problem statement from the given sample input and output.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a string consisting only of lowercase English alphabets and an integer K.

Output Format
For each test case, print the desired output, separated by a new line.

Constraints
1 <= T <= 1000
1 <= len(str) <= 1000
0 <= k <= 100000

Example
Input
2
smart 3
interviews 10

Output
vpduw
sxdobfsogc'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    s,k=map(str,input().strip().split())
    k=int(k)
    ans=''
    for i in s:
        index=ord(i) - ord('a')
        index = index + k
        index=index%26
        index+=ord('a')
        ans+=chr(index)
    print(ans)
