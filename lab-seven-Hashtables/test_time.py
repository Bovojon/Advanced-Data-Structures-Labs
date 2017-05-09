'''
Jon

test_time.py

'''

import time
from own_hashtable import HashTable

def build_own_hashtable():
    own_hash = HashTable(5)
    keys = [2,91,36,10]
    values = ["Jon", "Honglie", "Max", "Ash"]
    for i in range(0, len(keys)):
        own_hash.insert(keys[i], values[i])

def build_dict():
    dictionary = {}
    keys = [2,91,36,10]
    values = ["Jon", "Honglie", "Max", "Ash"]
    for i in range(0, len(keys)):
        dictionary[keys[i]] = values[i]


def time_deletes():
    # Build own hash table
    own_hash = HashTable(5)
    keys = [2,91,36,10]
    values = ["Jon", "Honglie", "Max", "Ash"]
    for i in range(0, len(keys)):
        own_hash.insert(keys[i], values[i])

    # Build dict hash table
    dictionary = {}
    keys = [2,91,36,10]
    values = ["Jon", "Honglie", "Max", "Ash"]
    for i in range(0, len(keys)):
        dictionary[keys[i]] = values[i]

    # Time deletion for own hash table
    start_time_own = time.time()
    own_hash.remove(36)
    end_time_own = time.time()
    total_time_own = end_time_own - start_time_own

    # Time deletion for dictionary
    start_time_dict = time.time()
    del dictionary[36]
    end_time_dict = time.time()
    total_time_dict = end_time_dict - start_time_dict

    # Print results
    print("\n")
    print("Time taken to delete key 36 with my own hash table: ")
    print(total_time_own)
    print("\n")
    print("Time taken to delete key 36 with Python's dict: ")
    print(total_time_dict)
    print("\n")



if __name__ == '__main__':

    start_time_own = time.time()
    build_own_hashtable()
    end_time_own = time.time()
    total_time_own = end_time_own - start_time_own

    print("\n")
    print("Time taken to build my own hash table: ")
    print(total_time_own)
    print("\n")


    #####################

    start_time_dict = time.time()
    build_dict()
    end_time_dict = time.time()
    total_time_dict = end_time_dict - start_time_dict

    print("\n")
    print("Time taken to build hash table with Python's dict: ")
    print(total_time_dict)
    print("\n")

    #####################
    time_deletes()
