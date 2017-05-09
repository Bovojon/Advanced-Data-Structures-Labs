"""
Jon Abdulloev

splay-test.py

"""


import sys
import unittest
import copy
from splay_tree import SplayTreeMap

# Testing using pyhton's unittest class
class TestSplayTree(unittest.TestCase):
    
    # Build the splay tree to test
    def __init__(self, *args, **kwargs):
        super(TestSplayTree, self).__init__(*args, **kwargs)
        self.splaytree = SplayTreeMap()
        self.arr = [30, 40, 24, 58, 48, 26, 11, 13]
        self.array = [25, 91, 36, 30, 21, 17, 57, 31]
        for i in range(0,len(self.arr)):
            self.splaytree[self.arr[i]] = self.array[i]
            
# LOOKUP TESTS            
    # Get the ROOT key
    def test_getRootKey(self):
        self.assertEqual(self.splaytree.root().key(), 13)
        
    # Get key before the ROOT
    def test_getBeforeRoot(self):
        self.beforeRoot = self.splaytree.before(self.splaytree.root())
        #self.assertEqual(self.beforeRoot.key(), 11)
        self.assertEqual(self.splaytree.before(self.splaytree.root()).key(), 11)

    # Get key after the ROOT
    def test_getAfterRoot(self):
        self.afterRoot = self.splaytree.after(self.splaytree.root())
        self.assertEqual(self.afterRoot.key(), 24)
        
    # Get the LAST key
    def test_getLastKey(self):
        self.assertEqual(self.splaytree.last().key(), 58)
        
    # Lookup 11 and test if it is the root after the lookup
    def test_lookupEleven(self):
        self.assertTrue(self.splaytree.find_position(11))
        self.assertEqual(self.splaytree.root().key(), 11)
        
        
# INSERT TESTS 
    # Insert into splay tree (25, 100) and test if root key is 25 after insertion
    def test_insert_twen_five(self):
        self.splaytree[25] = 100
        self.assertEqual(self.splaytree.root().key(), 25)
        
    # Insert into splay tree (9, 101) and test if root key is 9 after insertion
    def test_insert_nine(self):
        self.splaytree[9] = 101
        self.assertEqual(self.splaytree.root().key(), 9)
    
    # Insert into splay tree (56, 102) and test if root key is 25 after insertion
    def test_insert_fifty_six(self):
        self.splaytree[56] = 102
        self.assertEqual(self.splaytree.root().key(), 56)
        
    # Insert into splay tree (12, 103) and test if root key is 25 after insertion
    def test_insert_twelve(self):
        self.splaytree[12] = 103
        self.assertEqual(self.splaytree.root().key(), 12)
        
# DELETE TESTS
    # Delete internal node with key 26 - root key must be 24 after deletion
    def test_delItem_internal(self):
        # Check if new tree with root 13 if built
        self.assertEqual(self.splaytree.root().key(), 13)
        del self.splaytree[26]
        self.assertEqual(self.splaytree.root().key(), 24)
        
    # DELETE root node - check if root has key 11 after deletion
    def test_delete_root(self):
        rootItem = self.splaytree.root()
        self.splaytree.delete(rootItem)
        self.assertEqual(self.splaytree.root().key(), 11)
    
    # Delete the last and check if new root has key 48 after deletion
    def test_delete_last(self):
        del self.splaytree[58]
        self.assertEqual(self.splaytree.root().key(), 48)
        
# Other Trivial Tests from BST:
    # Find the node with maximum key
    def test_find_max(self):
        self.assertEqual(self.splaytree.find_max(), (58, 30))
    
    # Find the node with minimum key
    def test_find_min(self):
        self.assertEqual(self.splaytree.find_min(), (11, 57))
        
    # Find the node with greatest key strictly less than k = key
    def test_find_lt(self):
        self.assertTrue(self.splaytree.find_lt(40), 30)
                      
    # Find the node with least key strictly greater than k.
    def test_find_gt(self):
        self.assertEqual(self.splaytree.find_gt(48), (58,30))


 
        
# Before every test build a new tree
    def setUp(self):
        #Make deepcopy
        self.splaytree = copy.deepcopy(self.splaytree)
        print("New tree is built!")


# After every test delete the tested tree
    def tearDown(self):
        self.splaytree = None
        print("Tree is deleted!")
        #The following lines of code have been commented out - they test if the splay tree is actually deleted
        #keyOne = self.splaytree.root().key()
        #print(keyOne)

    
        

if __name__ == '__main__': 

    unittest.main()
    sys.exit(0)
    