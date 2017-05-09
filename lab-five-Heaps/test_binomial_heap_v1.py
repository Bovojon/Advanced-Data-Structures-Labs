import unittest
from binomial_Tree_Heap import BinomialHeap


class Test_BinomialHeap(unittest.TestCase):

    def setUp(self):
        self.BinomialHeap = BinomialHeap()
        key = [2,91,36,10,21,17,57]
        for i in range (0, len(key)):
            self.BinomialHeap.insert(key[i])

        self.empty_BinomialHeap = BinomialHeap()

        self.treeOther = BinomialHeap()
        keyOther = [4, 19, 63, 11, 12, 71, 75]
        for i in range(0, len(keyOther)):
            self.treeOther.insert(keyOther[i])

    def tearDown(self):
        del self.BinomialHeap
        del self.empty_BinomialHeap
        print("Tested Binomial Heap is deleted!")


# Find min tests
    def test_find_min(self):
        self.assertEqual(self.BinomialHeap.find_min(), 2)
        self.assertEqual(self.empty_BinomialHeap.find_min(), 10000)

# Deletion tests
    def test_remove_min(self):
        self.BinomialHeap.remove_min()
        self.assertEqual(self.BinomialHeap.minimum, 10)

# Insertion tests
    def test_insert_min(self):
        self.BinomialHeap.insert(1)
        self.assertEqual(self.BinomialHeap.minimum, 1)

    def test_insert_median(self):
        self.BinomialHeap.insert(19)
        self.assertEqual(self.BinomialHeap.minimum, 2)


    def test_multiple_insert(self):
        self.assertEqual(len(self.empty_BinomialHeap.trees),0)
        self.assertEqual(self.empty_BinomialHeap.elements, 0)

        self.empty_BinomialHeap.insert(6)
        self.empty_BinomialHeap.insert(8)

        self.assertEqual(len(self.empty_BinomialHeap.trees),2)
        self.assertEqual(self.empty_BinomialHeap.elements, 2)

        self.assertEqual(len(self.BinomialHeap.trees), 3)
        self.assertEqual(self.BinomialHeap.elements, 7)


# Merge tests
    def test_merge(self): # Over
        self.BinomialHeap.merge(self.treeOther)
        self.assertEqual(self.BinomialHeap.minimum, 2)



if __name__ == '__main__':
    unittest.main()
