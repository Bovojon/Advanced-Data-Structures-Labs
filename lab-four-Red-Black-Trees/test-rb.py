"""
Jon Abdulloev

test-rb.py

"""


import sys
import copy
import unittest
from bst import TreeMap
from rbtree import RedBlackTreeMap


class TestRedBlackTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestRedBlackTree, self).__init__(*args, **kwargs)
        self.tree = RedBlackTreeMap()
        self.arr = [32, 9, 16, 4, 52, 72, 67, 2, 97, 12]
        self.array = [25, 91, 36, 30, 21, 17, 57, 31, 89, 18]
        for i in range(0,len(self.arr)):
            self.tree[self.arr[i]] = self.array[i]


# Lookup tests
    # Lookup root
    def test_getRootWithRoot(self):
        self.assertFalse(self.tree.isRed(self.tree.root()))
        self.assertEqual(self.tree.root().key(), 16)

    # Lookup last element
    def test_getLast(self):
        self.assertTrue(self.tree.isRed(self.tree.last()))
        self.assertEqual(self.tree.last().key(), 97)

    # Lookup leaf key 32
    def test_lookup_leaf(self):
        self.assertFalse(self.tree.isRed( self.tree.find_position(32) ))
        self.assertEqual(self.tree.find_position(32).value(), 25)

    # Lookup internal key 52
    def test_lookup_internal(self):
        self.assertTrue(self.tree.isRed( self.tree.find_position(52) ))
        self.assertEqual(self.tree.find_position(52).value(), 21)

    # Lookup non-existent node with key-value pair (200, 67)
    def test_lookup_position_no_exists(self):
        self.assertRaises((AssertionError, TypeError), self.tree.find_position(200).value(), 67)


# Deletion tests
    # Delete root
    def test_delete_root(self):
        root = self.tree.root()
        self.assertRaises(AssertionError, self.tree.delete(root))
        # Check if after deletion root has key
        self.assertEqual(self.tree.root().key(), 12)

    # Delete last element
    def test_delete_last(self):
        last = self.tree.last()
        self.assertRaises(AssertionError, self.tree.delete(last))

    # Delete leaf 9
    def test_delete_leaf(self):
        leaf = self.tree.find_position(9)
        self.assertRaises(AssertionError, self.tree.delete(leaf))

    # Delete internal 52
    def test_delete_internal(self):
        internal = self.tree.find_position(52)
        self.assertRaises(AssertionError, self.tree.delete(internal))
        # Check if after deletion node with key 67 is red
        node67 = self.tree.find_position(67)
        self.assertTrue(self.tree.isRed(node67))

    # Delete non-existent node with key 300
    def test_delete_no_exists(self):
        non = self.tree.find_position(300)
        self.assertRaises(AssertionError, self.tree.delete(non))


# Insertion tests
    # Insert (25, 100) and test if its is red
    def test_insert_twen_five(self):
        self.tree[25] = 100
        self.assertTrue(self.tree.isRed( self.tree.find_position(25) ))
        self.assertEqual(self.tree.find_position(25).value(), 100)

    # Insert (77, 101) and test if it is red
    def test_insert_nine(self):
        self.tree[77] = 101
        self.assertTrue(self.tree.isRed( self.tree.find_position(77) ))
        self.assertEqual(self.tree.find_position(77).value(), 101)

    # Insert (56, 102) and test if it is red
    def test_insert_fifty_six(self):
        self.tree[56] = 102
        self.assertTrue(self.tree.isRed( self.tree.find_position(56) ))
        self.assertEqual(self.tree.find_position(56).value(), 102)

    # Insert (45, 103) and test if it is red
    def test_insert_twelve(self):
        self.tree[45] = 103
        self.assertTrue(self.tree.isRed( self.tree.find_position(45) ))
        self.assertEqual(self.tree.find_position(45).value(), 103)

# Other Trivial Tests from BST:
    # Find the node with maximum key
    def test_find_max(self):
        self.assertEqual(self.tree.find_max(), (97, 89))

    # Find the node with minimum key
    def test_find_min(self):
        self.assertEqual(self.tree.find_min(), (2, 31))

    # Find the node with greatest key strictly less than k = key
    def test_find_lt(self):
        self.assertTrue(self.tree.find_lt(32), (16,36))

    # Find the node with least key strictly greater than k.
    def test_find_gt(self):
        self.assertEqual(self.tree.find_gt(32), (52,21))

    # Get position BEFORE last node
    def test_before_last(self):
        lastItem = self.tree.last()
        self.assertEqual(self.tree.before(lastItem).key(), 72)

    # Get position before an internal node - use method find_position() to find position of internal node
    def test_before_internal(self):
        internalItem = self.tree.find_position(52)
        self.assertEqual(self.tree.before(internalItem).key(), 32)




# Before every test build a new tree
    def setUp(self):
        #Make deepcopy
        self.tree = copy.deepcopy(self.tree)
        print("New Rb tree is built!")


# After every test delete the tested tree
    def tearDown(self):
        self.tree = None
        print("Tested RB Tree is deleted!")



if __name__ == '__main__':

    unittest.main()
    sys.exit(0)
