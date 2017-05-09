import unittest
from Binomial_Tree_Heap import BinomialHeap

class Test_BinomialHeap (unittest.TestCase):
	def setUp(self):
	#------ create a BinomialHeap each time
		self.BinomialHeap = BinomialHeap()
		key = [2,91,36,10,21,17,57]
		for i in range (0, len(key)):
			self.BinomialHeap.insert(key[i])					# check if insert() works
	#-------create an empty BinomialHeap
		self.emy_BinomialHeap = BinomialHeap()

	def tearDown(self):
	#------ clear the BinomialHeap after each testCase
		del self.BinomialHeap
		del self.emy_BinomialHeap


	#------ public methods
	def test_get_min(self):
		self.assertEqual(self.BinomialHeap.get_min(), 2)
		# check the empty binomialheap
		self.assertEqual(self.emy_BinomialHeap.get_min(), 10000)

	def test_insert(self):
		self.assertEqual(len(self.emy_BinomialHeap.trees),0) 	# check the numbers of trees before insert
		self.assertEqual(self.emy_BinomialHeap.elements, 0)		# check the elements before insert
		self.emy_BinomialHeap.insert(6)
		self.emy_BinomialHeap.insert(8)
		self.assertEqual(len(self.emy_BinomialHeap.trees),2)	# check the numbers of trees after insert
		self.assertEqual(self.emy_BinomialHeap.elements, 2)     # check the elements after insert
		# check the BinomialHeap which is built by insert()
		self.assertEqual(len(self.BinomialHeap.trees), 3)
		self.assertEqual(self.BinomialHeap.elements, 7)
		self.assertEqual(self.BinomialHeap.min, 2)
		self.assertEqual(self.BinomialHeap.min_tree_order, 2)

	def test_delete_min(self):
		self.BinomialHeap.delete_min()
		self.assertEqual(self.BinomialHeap.min, 10)				# check the new min after delete
		self.assertEqual(self.BinomialHeap.elements, 6)			# check the new elements after delete
		self.assertEqual(len(self.BinomialHeap.trees), 3)		# check the number of trees after delete
		# to test more
		self.BinomialHeap.delete_min()
		self.assertEqual(self.BinomialHeap.min, 17)				# check the new min after delete
		self.assertEqual(self.BinomialHeap.elements, 5)			# check the new elements after delete
		self.assertEqual(len(self.BinomialHeap.trees), 3)		# check the number of trees after delete

	def test_merge(self):
		self.emy_BinomialHeap.insert(1)
		self.emy_BinomialHeap.insert(19)
		self.emy_BinomialHeap.insert(63)
		self.emy_BinomialHeap.insert(11)
		self.emy_BinomialHeap.insert(12)
		self.BinomialHeap.merge(self.emy_BinomialHeap)
		self.assertEqual(self.BinomialHeap.min, 1)				# check if the new min is updated
		self.assertEqual(self.BinomialHeap.elements, 12)		# check the new elements
		self.assertEqual(len(self.BinomialHeap.trees), 4)		# check the new number of trees

	def test_decrease_key(self):
		a = self.emy_BinomialHeap.decrease_key(9,2)				# check if the error can be recognized.
		self.assertEqual(a, None)
		self.BinomialHeap.decrease_key(2,1)					    # check if the new min is updated.
		self.assertEqual(self.BinomialHeap.min,1)
		# more tests
		self.BinomialHeap.decrease_key(17,16)
		keys = []
		for i in self.BinomialHeap.trees:
			keys.append(i.value)
			for i in i.child:
				keys.append(i.value)
		self.assertNotIn(17, keys)								# check if old key doesnt exist
		self.assertIn(16, keys)									# check if new key exist


if __name__ == '__main__' :
		unittest.main()
