'''Given 2 strings A and B, print all the interleavings of the 2 strings. An interleaved string of given two strings preserves the order of characters in individual strings and uses all the characters of both the strings. For simplicity, you can assume that the strings have unique characters.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each containing 2 space-separated strings A and B.

Output Format
For each test case, print the test case number, followed by the interleavings of the 2 strings in a sorted order, separated by a new line.

Constraints
1 <= T <= 100
'a' <= A[i], B[i] <= 'z'
1 <= len(A), len(B) <= 10

Example
Input
2
nkb gl
bn zh

Output
Case #1:
glnkb
gnkbl
gnklb
gnlkb
ngkbl
ngklb
nglkb
nkbgl
nkgbl
nkglb
Case #2:
bnzh
bzhn
bznh
zbhn
zbnh
zhbn'''

def solution(str1,str2,r_index,s1_index,s2_index,result,my_solution):
    if s1_index==0 and s2_index==0:
        result=''.join(result)
        my_solution.append(result)
    
    if s1_index!=0:
        result[r_index] = str1[0]
        solution(str1[1:],str2,r_index+1,s1_index-1,s2_index,result,my_solution)

    if s2_index!=0:
        result[r_index] = str2[0]
        solution(str1,str2[1:],r_index+1,s1_index,s2_index-1,result,my_solution)

t=int(input())
for _ in range(t):
    a,b=map(str,input().split())
    my_solution=[]
    result=[''] * (len(a) + len(b))
    solution(a,b,0,len(a),len(b),result,my_solution)
    print('Case #{}:'.format(_+1))
    my_solution.sort()
    for i in my_solution:
        print(i)
    print()
