## UDACITY
## 7/30/2019
## Hashing


"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter

class HashTable(object):
    def __init__(self):
        # willing to sacrifice space to minimize collisions
        self.table = [None]*10000

    # NOTE: hash table is just Python list. index of the list is the hash value
    # E.g. H('UDACITY') = 8568. Thus, table[8568] == 'UDACITY'
    # Using index to lookup value => lookup is O(1) as is the case w/ hash table
    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            # chaining
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
