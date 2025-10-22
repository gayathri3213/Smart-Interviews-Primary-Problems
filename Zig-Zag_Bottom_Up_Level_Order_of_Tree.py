'''Given an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree in a zig-zag fashion, not top-down, but bottom-up. Assume the root is at level-1, zig-zag means that nodes at even levels will be printed left to right and the nodes at odd levels will be printed from right to left.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the bottom-up Level Order Traversal of the Binary Search Tree in a zig-zag fashion, separated by a newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
3
5
1 2 3 4 5
5
3 2 4 1 5
7
4 5 15 0 1 7 17

Output
5 4 3 2 1
5 1 2 4 3
7 17 15 1 0 5 4'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def bstinsert(tree,val):
    if tree is None:
        return Node(val)
    if val<tree.val:
        tree.left=bstinsert(tree.left,val)
    else:
        tree.right=bstinsert(tree.right,val)
    return tree

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    tree=Node(a[0])
    for i in range(1,n):
        tree=bstinsert(tree,a[i])
    hm={}
    def bottom_up_level_order(root,level):
        if root is None:
            return 
        if level in hm:
            hm[level].append(root.val)
        else:
            hm[level]=[root.val]
        bottom_up_level_order(root.left,level+1)
        bottom_up_level_order(root.right,level+1)
    bottom_up_level_order(tree,0)
    my_keys=hm.keys()
    my_keys=sorted(my_keys,reverse=True)
    for level in my_keys:
        nodes=hm[level]
        if (level+1)%2==0:
            nodes.sort()
        else:
            nodes=sorted(nodes,reverse=True)
        for n in nodes:
            print(n,end=' ')
    print()
