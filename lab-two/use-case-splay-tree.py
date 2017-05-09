"""
Jon Abdulloev

use-cases.py

"""
import time
from avl_tree import AVLTreeMap
from bst import TreeMap
from splay_tree import SplayTreeMap

if __name__ == '__main__':

    # Use case implemented in Splay tree
    print("Use case implemented in Splay tree")
    print("\n")
    splaytree = SplayTreeMap()
    arrNums = [123, 456, 789, 212, 345, 678, 910, 112]
    arrNames = ["Jon", "Mike", "Cane", "Max", "Jack", "James", "Don", "Gimi"]
    for i in range(0,len(arrNums)):
        splaytree[arrNums[i]] = arrNames[i]

    # Time insertion
    startOne = time.time()
    splaytree[978] = "Sarah"
    end1 = time.time()
    timeInsertion1 = end1 - startOne
    print("Time insertion for key 978: ")
    print(timeInsertion1)
    print("\n")

    # Time deletion
    startTwo = time.time()
    del splaytree[978]
    end2 = time.time()
    timeDeletion2 = end2 - startTwo
    print("Time Deletion for key 978: ")
    print(timeDeletion2)
    print("\n")

     # Time lookup
    splaytree.find_position(212)
    startThree = time.time()
    splaytree.find_position(212)
    end3 = time.time()
    timeLookup3 = end3 - startThree
    print("Time Lookup for key 212 after looking it up: ")
    print(timeLookup3)
    print("\n")

    print("####################################")
    print("\n")


    # Use case implemented in Binary Search tree
    print("Use case implemented in Binary Search tree")
    print("\n")
    bstTree = TreeMap()
    arrNums = [123, 456, 789, 212, 345, 678, 910, 112]
    arrNames = ["Jon", "Mike", "Cane", "Max", "Jack", "James", "Don", "Gimi"]
    for i in range(0,len(arrNums)):
        bstTree[arrNums[i]] = arrNames[i]

    # Time insertion
    startFour = time.time()
    bstTree[978] = "Sarah"
    end4 = time.time()
    timeInsertion4 = end4 - startFour
    print("Time insertion for key 978: ")
    print(timeInsertion4)
    print("\n")

    # Time deletion
    startFive = time.time()
    del bstTree[978]
    end5 = time.time()
    timeDeletion5 = end5 - startFive
    print("Time Deletion for key 978: ")
    print(timeDeletion5)
    print("\n")

     # Time lookup
    bstTree.find_position(212)
    startSix = time.time()
    bstTree.find_position(212)
    end6 = time.time()
    timeLookup6 = end6 - startSix
    print("Time Lookup for key 212 after looking it up: ")
    print(timeLookup6)
    print("\n")

    print("####################################")
    print("\n")


    # Use case implemented in AVL tree
    print("Use case implemented in AVL Tree")
    print("\n")
    avlTree = AVLTreeMap()
    arrNums = [123, 456, 789, 212, 345, 678, 910, 112]
    arrNames = ["Jon", "Mike", "Cane", "Max", "Jack", "James", "Don", "Gimi"]
    for i in range(0,len(arrNums)):
        avlTree[arrNums[i]] = arrNames[i]

    # Time insertion
    startSeven = time.time()
    avlTree[978] = "Sarah"
    end7 = time.time()
    timeInsertion7 = end7 - startSeven
    print("Time insertion for key 978: ")
    print(timeInsertion7)
    print("\n")

    # Time deletion
    startEight = time.time()
    del avlTree[978]
    end8 = time.time()
    timeDeletion8 = end8 - startEight
    print("Time Deletion for key 978: ")
    print(timeDeletion8)
    print("\n")

     # Time lookup
    avlTree.find_position(212)
    startNine = time.time()
    avlTree.find_position(212)
    end9 = time.time()
    timeLookup9 = end9 - startNine
    print("Time Lookup for key 212 after looking it up: ")
    print(timeLookup9)
    print("\n")

    print("####################################")
