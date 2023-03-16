"""Interview Question 2
Design a data structure for a cache

Design and implement a data structure for a cache, which has the following functions:
get(key)
Return the value associated with the specified key if it exists in the cache, else
return -1 .
put(key, value, weight)
Associate value with key in the cache, such that value might be later retrieved by
get(key) .
Cache has a fixed capacity, and when such capacity is reached, key with the least
score must be invalidated until the number of key s falls within cache capacity. The
score is calculated as follows:
weight ∕ [ln(current_time - last_accessed_time + 1) + 1]
Implementation of the cache should be optimized on the time complexity of get(key) .
For example, the average time complexity of get(key) could be constant.
For the purpose of implementing the cache, you could assume that common data
structures, such as arrays, different types of lists, and hash tables, are available.
At the end of the answer, give and explain the computational complexity of get(key) and
put(...) in Big O notation.
"""
import heapq
import time
import math


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.scores = []
        self.last_accessed = {}

    def get(self, key):
        if key in self.cache:
            value, weight, last_accessed_time = self.cache[key]
            score = self.calculate_score(weight, last_accessed_time)
            heapq.heappush(self.scores, (score, key))
            self.last_accessed[key] = time.time()
            return value
        else:
            return -1

    def put(self, key, value, weight):
        if key in self.cache:
            # Update existing key
            _, _, last_accessed_time = self.cache[key]
            score = self.calculate_score(weight, last_accessed_time)
            heapq.heappush(self.scores, (score, key))
            self.last_accessed[key] = time.time()
            self.cache[key] = (value, weight, last_accessed_time)
        else:
            # Add new key
            if len(self.cache) == self.capacity:
                # Remove least recently used key
                while self.scores:
                    _, least_key = heapq.heappop(self.scores)
                    if least_key in self.cache:
                        del self.cache[least_key]
                        del self.last_accessed[least_key]
                        break
            score = self.calculate_score(weight, 0)
            heapq.heappush(self.scores, (score, key))
            self.last_accessed[key] = time.time()
            self.cache[key] = (value, weight, 0)

    def calculate_score(self, weight, last_accessed_time):
        current_time = time.time()
        time_diff = current_time - last_accessed_time + 1
        return weight / (math.log(time_diff) + 1)


# Create a cache with a capacity of 10
cache = Cache(10)

# Add some values to the cache
cache.put('key1', 'value1', 1)
cache.put('key2', 'value2', 2)
cache.put('key3', 'value3', 3)

# Get a value from the cache
value = cache.get('key1')
print(value)  # Output: 'value1'

# Add a new value that exceeds the cache capacity
for i in range(90,100):
    cache.put(f'key{i}', f'value{i}', i+1)

# Get a value that was removed due to cache capacity limit
value = cache.get('key1')
print(value)  # Output: -1 (key1 was removed due to cache capacity limit)
