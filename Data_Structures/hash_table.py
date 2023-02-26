"""Hash Tables

A hash table is a data structure that maps keys to values using a
hash function., providing consistant-time across to the elements.

A common use of a hash table is to implement a dictionary or a 
mapping between keys and values. For example, you might use a hash 
table to implement a phone book, where each person's name is a key 
that maps to their phone number.

In this example, we define a HashTable class that represents a hash 
table data structure, and provides methods for setting and getting 
key-value pairs. The _hash method is used to generate a hash code 
for a given key, which is used to index into the underlying array. 
If two keys hash to the same index, they are stored in a linked 
list at that index.
"""
class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)


# create new hash table
hash_table: HashTable = HashTable()

# add a new key-value pair
hash_table.set('apple', 5)

print(hash_table.get('apple'))

# try to retrieve a key that doesn't exist
print(hash_table.get('pears'))


# Output
# 5
# KeyError: 'pears'