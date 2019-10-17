#! /usr/bin/python

# To use this class, import relative path by adding the following to your code: 
# import sys
# sys.path.append('..')


class BinaryTree(object):
    def __init__(self,rootObj):
        self.val = rootObj
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            insert_branch = BinaryTree(newNode) # create new node object
            insert_branch.left = self.left # attach current node left to new node object
            self.left = insert_branch # attach new left node object to current root 

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            insert_branch = BinaryTree(newNode)
            insert_branch.right = self.right
            self.right = insert_branch

    def getright(self):
        return self.right

    def getleft(self):
        return self.left

    def setRootVal(self,obj):
        self.val = obj

    def getRootVal(self):
        return self.val