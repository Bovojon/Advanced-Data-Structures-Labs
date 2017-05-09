"""
Jon Abdulloev

use-cases.py

"""

from avl_tree import AVLTreeMap
from bst import TreeMap

if __name__ == '__main__':
    
    # Use case implemented in bst 
    print("Use case implemented in bst")
    BSTtree = TreeMap()
    arrRanks = [6, 2, 4, 3, 7, 5, 8, 9, 0, 1]
    arrColleges = ["Harvard", "MIT", "Stanford", "Colby", "Earlham", "Purdue", "IUPUI", "Hamilton", "Depauw", "Carlton"]
    for i in range(0,len(arrRanks)):
        BSTtree[arrRanks[i]] = arrColleges[i]

    print("The college at 5th place is "+BSTtree[5])
    lastItem = BSTtree.last()
    print("The last college is "+lastItem.value())
    print("The first is "+BSTtree.root().value())
    print("The college at position with key 2 is "+BSTtree.find_position(2).value())
    print("Traversing the BST tree gives: ")
    print("....")
    for i in iter(BSTtree):
        print(BSTtree[i])
    
    
    
    print("####################################")
    
    # Use case implemented in avl 
    print("Use case implemented in avl")
    AVLtree = TreeMap()
    arrRanks = [6, 2, 4, 3, 7, 5, 8, 9, 0, 1]
    arrColleges = ["Harvard", "MIT", "Stanford", "Colby", "Earlham", "Purdue", "IUPUI", "Hamilton", "Depauw", "Carlton"]
    for i in range(0,len(arrRanks)):
        AVLtree[arrRanks[i]] = arrColleges[i]

    print("The college at 5th place is "+AVLtree[5])
    lastItem = AVLtree.last()
    print("The last college is "+lastItem.value())
    print("The first is "+AVLtree.root().value())
    print("The college at position with key 2 is "+AVLtree.find_position(2).value())
    print("Traversing the AVL tree gives: ")
    print("....")
    for i in iter(AVLtree):
        print(AVLtree[i])
    
    print("####################################")
    
    
    
    