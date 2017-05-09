"""
Jon Abdulloev

use-cases.py

This use-case is of a Completely Fair Scheduler (CFS) of a Linux Kernel
- The nodes are indexed by keys which are the amount of time that a process has gotten
- The values are the names of the processes. 

"""
import time
import timeit
import random
from rbtree import RedBlackTreeMap
import bst_use_case

def build_RB():
    rand_array = []
    for j in range(120):
        j = random.randint(1, 10000)
        rand_array.append(j)
        
    RBTree = RedBlackTreeMap() 
    for i in range(0, len(rand_array)):
        RBTree[rand_array[i]] = "Arbitrary Process"
    
    return RBTree, rand_array
    
    
def lookup_RB(RBTree, rand_array):
    for i in rand_array:
        RBTree.find_position(i)
        
        
def delete_RB(RBTree, rand_array):
    for i in rand_array:
        del RBTree[i]

    
def time_RB():
    
    RB_times = []
    
    # Time insertions of 120 items
    start1 = time.time()
    RBTree, rand_array = build_RB()
    end1 = time.time()
    RB_Insertion = end1 - start1

    RB_times.append(RB_Insertion)
    
    
    # Time Lookups of 120 items
    start2 = time.time()
    lookup_RB(RBTree, rand_array)
    end2 = time.time()
    RB_Lookup = end2 - start2 

    RB_times.append(RB_Lookup)
  
    
    
    # Time deletions of 120 items
    start3 = time.time()
    delete_RB(RBTree, rand_array)
    end3 = time.time()
    RB_Deletion = end3 - start3

    RB_times.append(RB_Deletion)
    
    print("Is the tree is empty? ")
    print(RBTree.is_empty())
    
    return RB_times
    
    

def write_to_file(RB_times, BST_times):
    ft = open("results.dat", "w")
    
    ft.write("The time taken (in seconds) for 120 insertions by a binary search tree is %s. \n" % BST_times[0])
    ft.write("The time taken (in seconds) for 120 insertions by a red-black tree is %s. \n" % RB_times[0])
    
    ft.write("\n")
    
    ft.write("The time taken (in seconds) for 120 lookups by a binary search tree is %s. \n" % BST_times[1])
    ft.write("The time taken (in seconds) for 120 lookups by a red-black tree is %s. \n" % RB_times[1])
    
    ft.write("\n")
    
    ft.write("The time taken (in seconds) for 120 deletions by a binary search tree is %s. \n" % BST_times[2])
    ft.write("The time taken (in seconds) for 120 deletions by a red-black tree is %s. \n" % RB_times[2])
    
    ft.close()
    
    
        

if __name__ == '__main__':
    BST_times = bst_use_case.time_BST()    
    RB_times = time_RB()
    
    print(BST_times)
    print(RB_times)
    
    
    write_to_file(RB_times, BST_times)
    
   
    
    
    
    