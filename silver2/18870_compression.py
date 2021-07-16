import sys
from collections import deque

N = int(sys.stdin.readline())
coor_sorted = list(map(int, sys.stdin.readline().rstrip().split()))
coor = coor_sorted.copy()
coor_sorted.sort()
rank = dict()
s = 0

for i in range(N):
    if i == 0:
        rank.update({coor_sorted[i]:s})
        s += 1
    elif coor_sorted[i] == coor_sorted[i-1]:
        continue
    else:
        rank.update({coor_sorted[i]:s})
        s += 1

for i in range(N):
    print(rank.get(coor[i]), end=' ')

# def inorder(ptr):
#     global rank
#     if ptr:
#         inorder(ptr.leftchild)
#         coor_rank.update({ptr.data: rank})
#         rank += 1
#         inorder(ptr.rightchild)

# def modifysearch(ptr, data):
#     if ptr.data > data:
#         if ptr.leftchild == None:
#             return ptr
#         else:
#             return modifysearch(ptr.leftchild, data)
#     elif ptr.data < data:
#         if ptr.rightchild == None:
#             return ptr
#         else:
#             return modifysearch(ptr.rightchild, data)
#     else:
#         return None

# class Node:
#     def __init__ (self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# class binarytree:
#     def __init__ (self, data):
#         self.pointer = Node(data)

#     def insert(self, data):
#         temp = modifysearch(self.pointer, data)

#         if temp != None:
#             if data > temp.data:
#                 temp.rightchild = Node(data)
#             else:
#                 temp.leftchild = Node(data)
    
#     def rank(self):
#         inorder(self.pointer)

# binarydata = binarytree(coor[0])
# for i in range(1, N):
#     binarydata.insert(coor[i])

# binarydata.rank()

# for i in coor:
#     print(coor_rank.get(i), end=' ')