"""
Jon
test_hashtable.py

"""

import unittest
from own_hashtable import HashTable


class Test_HashTable(unittest.TestCase):

    def setUp(self):
        self.HashTable = HashTable(5)

        keys = [2,91,36,10]
        values = ["Jon", "Honglie", "Max", "Ash"]
        for i in range(0, len(keys)):
            self.HashTable.insert(keys[i], values[i])

# Test getitem
    def test_getitem(self):
        self.assertEqual(self.HashTable[2], "Jon")
        self.assertEqual(self.HashTable[91], "Honglie")
        self.assertEqual(self.HashTable[36], "Max")
        self.assertEqual(self.HashTable[10], "Ash")

# Test remove
    def test_remove(self):
        # Delete items that exist - must return None after deletion.
        self.assertFalse(self.HashTable.remove(2), None)
        self.assertTrue(self.HashTable.remove(91), None)
        # Delete keys that don't exist
        self.assertEqual(self.HashTable.remove(5), "No key found.")
        self.assertEqual(self.HashTable.remove(9), "No key found.")


if __name__ == '__main__':
    unittest.main()
