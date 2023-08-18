"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hashValue=(ord(string[0])*100)+ord(string[1]) # ascii value of first letter * 100 + ascii value of second letter
        self.table[hashValue]=string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashValue=(ord(string[0])*100)+ord(string[1])
        data=self.table[hashValue]
        if data:
            return hashValue 
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0])*100)+ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
print (hash_table.calculate_hash_value('TEST')) # Should be 8469

# Test lookup edge case
print (hash_table.lookup('TEST1')) # Should be -1

# Test store
hash_table.store('TEST1')
print (hash_table.lookup('TEST1')) # Should be 8469

# Test store edge case
hash_table.store('DATA')
print (hash_table.lookup('DATA')) # Should be 6865
