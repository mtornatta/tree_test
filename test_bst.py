#test_bst.py by Michael Tornatta
#Yong Bakos CS 261 10/29/18

import unittest
from bst import bst

class TestTree(unittest.TestCase):

#---------------------------------
#     Create an Empty Tree
#---------------------------------

#test if a new tree exists
    def test_empty_instantiation(self):
        new_tree = bst()
        self.assertTrue(new_tree != None)
#test if the tree has a parent element
    def test_for_parent_when_empty(self):
        new_tree = bst()
        self.assertTrue(new_tree.parent == None)
#test if the bst is the root (if parent is itself)
    def test_if_root(self):
        new_tree = bst()
        self.assertTrue(new_tree.is_root())
#test if it has any children (should not, empty tree)
    def test_for_child_when_empty(self):
        new_tree = bst()
        self.assertFalse(new_tree.has_child())

#test if it has a right child element (should not, empty tree)
    def test_for_right_when_empty(self):
        new_tree = bst()
        self.assertFalse(new_tree.has_right_child())

#test if it has a left child element (should not, empty tree)
    def test_for_left_when_empty(self):
        new_tree = bst()
        self.assertFalse(new_tree.has_left_child())

#test if it has a both a right and left child element (should not, empty tree)
    def test_for_both_when_empty(self):
        new_tree = bst()
        self.assertFalse(new_tree.has_both_children())

#---------------------------------------------
#  Create a Tree with left and right nodes
#---------------------------------------------

#test if you can create a bst with content
    def test_new_bst_with_value(self):
        new_tree = bst(20)
        self.assertTrue(new_tree.value != None)
#test what happens when you add an element larger than the parent
    def test_add_node_when_larger(self):
        new_tree = bst(20)
        larger_node = bst(21)
        new_tree.add(larger_node)
        self.assertTrue(new_tree.get_right_child().value == larger_node.value)
#test what happens when you add an element smaller than the parent
    def test_add_node_when_smaller(self):
        new_tree = bst(20)
        smaller_node = bst(19)
        new_tree.add(smaller_node)
        self.assertTrue(new_tree.get_left_child().value == smaller_node.value)
#check the parent of left
    def test_parent_of_left(self):
        new_tree = bst(20)
        smaller_node = bst(19)
        new_tree.add(smaller_node)
        self.assertTrue(new_tree.get_left_child().get_parent().value == new_tree.value)
#check the parent of right
    def test_parent_of_right(self):
        new_tree = bst(20)
        larger_node = bst(21)
        new_tree.add(larger_node)
        self.assertTrue(new_tree.get_right_child().get_parent().value == new_tree.value)

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
