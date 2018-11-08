#test_bst.py by Michael Tornatta
#Yong Bakos CS 261 10/29/18

import unittest
from bst import BinarySearchTree

class TestTree(unittest.TestCase):

    def test_empty_instantiation(self):
        BinarySearchTree()

if __name__ == '__main__':
    unittest.main()
