"""
Jon Abdulloev

avl-test.py

"""

import sys
import unittest
from avl_tree import AVLTreeMap


class TestAVLTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAVLTree, self).__init__(*args, **kwargs)
        self.tree = AVLTreeMap()
        self.arr = [32, 9, 16, 4, 52, 72, 67, 2, 97, 12]
        self.array = [25, 91, 36, 30, 21, 17, 57, 31, 89, 18]
        for i in range(0,len(self.arr)):
            self.tree[arr[i]] = self.array[i]

    # FAIL CASE - Check if bst is EMPTY - should return false
    def test_is_empty(self):
        self.assertTrue(self.tree.is_empty())         # Return true if method self.assertFalse(self.tree.is_empty()) used

#################################### Test positional methods
    # Get the FIRST element of bst
    def test_getFirst(self):
        self.assertTrue(self.tree.first())

    # Get the ROOT element of bst
    def test_getRootWithRoot(self):
        self.assertTrue(self.tree.root())

    # Check if getFirst() and getRoot() return same root
    def test_getRoot(self):
        self.assertEqual(self.assertTrue(self.tree.root()), self.assertTrue(self.tree.first()))

    # Get the LAST element of bst
    def test_getLast(self):
        self.assertEqual(self.tree.last().key(), 97)

    # Get the position of node with key 2 which exists in the tree
    def test_find_position_exists(self):
        self.assertEqual(self.tree.find_position(32).value(), 25)

    # FAIL CASE - Get the position of node with key 11 which does not exist in the tree
    def test_find_position_no_exists(self):
        self.assertTrue(self.tree.find_position(11))

#################################### Test BEFORE
    # Get position BEFORE last node
    def test_before_last(self):
        lastItem = self.tree.last()
        self.assertEqual(self.tree.before(lastItem).key(), 72)

    # FAIL CASE - Get position before root node - should return None
    def test_before_first(self):
        firstItem = self.tree.first()
        self.assertTrue(self.tree.before(firstItem))

    # Get position before an internal node - use method find_position() to find position of internal node
    def test_before_internal(self):
        internalItem = self.tree.find_position(4)
        self.assertTrue(self.tree.before(internalItem))
#################################### Test AFTER
    # FAIL CASE - Get position AFTER last node - should return None
    def test_after_last(self):
        lastItem = self.tree.last()
        self.assertTrue(self.tree.after(lastItem))

    # Get position AFTER root node
    def test_after_first(self):
        firstItem = self.tree.first()
        self.assertTrue(self.tree.after(firstItem))

    # Get position AFTER an internal node - use method find_position() to find position of internal node
    def test_after_internal(self):
        internalItem = self.tree.find_position(4)
        self.assertTrue(self.tree.after(internalItem))

#################################### Test ORDER of the binary search tree
    # Find the node with maximum key
    def test_find_max(self):
        self.assertEqual(self.tree.find_max(), (97, 89))

    # Find the node with minimum key
    def test_find_min(self):
        self.assertEqual(self.tree.find_min(), (2, 31))

    # Find the node with greatest key less than or equal to k = key
    def test_find_le(self):
        self.assertTrue(self.tree.find_le(3))

    # Find the node with greatest key strictly less than k = key
    def test_find_lt(self):
        self.assertTrue(self.tree.find_lt(5))

    # Find the node with least key greater than or equal to k
    def test_find_ge(self):
        self.assertTrue(self.tree.find_ge(3))

    # Find the node with least key strictly greater than k.
    def test_find_gt(self):
        self.assertTrue(self.tree.find_gt(0))


################################### Test public methods with SPECIAL SYNTAX
    def test_getItem(self):
        self.assertTrue(self.tree[4])

    # FAIL CASE - Delete node with key 52 - Must return 57 != 21
    def test_delItem(self):
        del self.tree[52]
        self.assertEqual(self.tree.find_position(52).value(), 21)


################################### Test DELETE method lastly because we need tree for other tests
    # FAIL CASE - DELETE Root node - Must return None
    def test_delete_root(self):
        firstItem = self.tree.first()
        self.assertTrue(self.tree.delete(firstItem))

    # FAIL CASE - DELETE last node - Must return None
    def test_delete_last(self):
        lastItem = self.tree.last()
        self.assertTrue(self.tree.delete(lastItem))

    # FAIL CASE - DELETE leaf node - Must return None
    def test_delete_leaf(self):
        leaf = self.tree.find_position(9)
        self.assertTrue(self.tree.delete(leaf))

    # FAIL CASE - DELETE internal node - Must return None
    def test_delete_internal(self):
        internal = self.tree.find_position(2)
        self.assertTrue(self.tree.delete(internal))




if __name__ == '__main__':

    treejon = AVLTreeMap()
    arr = [32, 9, 16, 4, 52, 72, 67, 2, 97, 12]
    array = [25, 91, 36, 30, 21, 17, 57, 31, 89, 18]
    for i in range(0,len(arr)):
        treejon[arr[i]] = array[i]

    #print(treejon[9])
    #print("--------------------")
    lastItem = treejon.last()
    #print(treejon.before(lastItem).key())
    #for i in iter(treejon):
        #print(treejon[i])
    for i in range(10):
        print("#########################")
    #print(treejon.find_max())

    #print(treejon.before(lastItem).key())
    #print(treejon.root())
    #print(treejon.find_position(2))


    unittest.main()
    sys.exit(0)
