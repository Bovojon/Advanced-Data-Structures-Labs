'''
Jon
own_hashtable.py

'''


class HashTable():

    # Initialize the HashTable properties
    def __init__(self, n):
        self.n = n          # hash table needs to be initialized with size n
        self.hash_table = [[] for i in range (0, self.n)] # Implement HashTable as a list of 2-tuples. The 2-tuples will consist of key-value pairs.


    # Get the size of the hash(self):
    def size(self):
        return self.n

    # Implement hash function to convert from integer/string to an integer in a specified range from 0 to size of hash table
    def hash_function(self, input_key):
        # If the input_key is an integer, simple return input_key%n as the hash code
        if isinstance(input_key, int):
            return(input_key%self.n)
        # If the input_key is a string, return the sum of the ASCII values of the letters mod n.
        else:
            sum_hash_values = 0
            for i in range(0, len(input_key)):
                sum_hash_values = sum_hash_values + ((i+1)*ord(input_key[i]))       # Multiple by (i+1) to have different hash values for anagrams. The function ord converts a character to it’s corresponding ASCII value
            return(sum_hash_values%self.n)


    # Use hash functions to insert input keys and values
    def insert(self, input_key, input_val):
        if isinstance(input_key, int) or isinstance(input_key, str):
            self.hash_table[self.hash_function(input_key)].append((input_key, input_val))


    # Get the value of the input_key
    def __getitem__(self, input_key):
        # Find the hash code for the input key
        if isinstance(input_key, int) or isinstance(input_key, str):
            hash_code = self.hash_function(input_key)
        for i in range(0, len(self.hash_table[hash_code])):
            if self.hash_table[hash_code][i][0] == input_key:
                return self.hash_table[hash_code][i][1]

    # In order to remove a key-value pair, find the value given the key. Then use del to remove and decrease size of hash table by 1.
    def remove(self, input_key):
        hash_code = self.hash_function(input_key)
        for i in range(0, len(self.hash_table[hash_code])):
            if self.hash_table[hash_code][i][0] == input_key:
                del self.hash_table[hash_code][i]
                self.n -= 1
                return None             # Return None if found and deleted.
        return("No key found.")         # Return "No key found." otherwise.
