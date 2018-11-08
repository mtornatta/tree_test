#test_bst.py by Michael Tornatta
#Yong Bakos CS 261 10/29/18

import unittest
from bst import bst

class TestTree(unittest.TestCase):

#---------------------------------
#     Create an Empty Tree
#---------------------------------
    def test_empty_instantiation(self):
        new_tree = bst()

#test if it has a parent (itself)
#test if the bst is the root (if parent is itself)
#test if it has potential for right and left child (should be empty)
#test for height value (should be 0)

#---------------------------------------------
#  Create a Tree with left and right nodes
#---------------------------------------------

#test if you can create a bst with content
#test what happens when you add an element smaller than the parent
#test what happens when you add an element larger than the parent
#check for left and right values after adding
#check for left and right parent (should be the root)
#check for height of the tree after adding a node

#-----------------------------------------------
#     Create a tree with more than one level
#-----------------------------------------------

#add more than one level to a Tree
#recurse through tree
#check height

#-----------------
#     Find
#-----------------

#compare value to see if it's larger or smaller than the root
#traverse down the side of the tree that goes in the right direction
#if you find the value stop and recurse back to the root
#if you reach the end of the tree return false to the root

#-----------------
#     Insert
#-----------------

#recurse down to value you want to insert after
#figure out if it goes on the left or right
#if the node has no child insert with nothing else
#if the node has a child make it the child of the current then make it the parent of the next

#-------------------
#     Traversal
#-------------------

#Pre: Root L R
#In: L Root R
#Post: L R Root

#-------------------
#     Deletion
#-------------------

#recurse down to element to delete
#de link the element
#re link elements

if __name__ == '__main__':
    unittest.main()
