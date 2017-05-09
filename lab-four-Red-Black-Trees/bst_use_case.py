import time
import timeit
import random
from bst import TreeMap

def build_BST():
    rand_array = []
    for j in range(120):
        j = random.randint(1, 10000)
        rand_array.append(j)
        
    BSTtree = TreeMap()
    for i in range(0, len(rand_array)):
        BSTtree[rand_array[i]] = "Arbitrary Process"
    
    return BSTtree, rand_array
    
    
def lookup_BST(BST, rand_array):
    for i in rand_array:
        BST.find_position(i)
        
        
def delete_BST(BSTtree, rand_array):
    for i in rand_array:
        del BSTtree[i]

    
    
def time_BST():
    
    BST_times = []
    
    # Time insertions of 120 items
    start1 = time.time()
    BSTtree, rand_array = build_BST()
    end1 = time.time()
    BST_Insertion = end1 - start1

    BST_times.append(BST_Insertion)
    
    
    # Time Lookups of 120 items
    start2 = time.time()
    lookup_BST(BSTtree, rand_array)
    end2 = time.time()
    BST_Lookup = end2 - start2 

    BST_times.append(BST_Lookup)
  
    
    
    # Time deletions of 120 items
    start3 = time.time()
    delete_BST(BSTtree, rand_array)
    end3 = time.time()
    BST_Deletion = end3 - start3

    BST_times.append(BST_Deletion)
    
    print("Is the tree is empty? ")
    print(BSTtree.is_empty())
    
    return BST_times
    