"""Time Based Key-Value Store

LEETCODE: 981
COMPANY:  Google

Design a time-based key-value data structure that can store 
multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the 
key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such 
that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value 
associated with the largest timestamp_prev. 
If there are no values, it returns "".

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]


Solution
- We will create a hashmap to store the key-value pairs, and also
  do a binary search on the timestamp in order to find our values.
- The value will be a list of val,time pairs associated with 
  each key.

  Key    Values <val, time>
  "foo"  [["bar", 1]]

- We want the logic to be able to select the closest timestamp
  lower or equal to the given timestamp in the list.
- So if we try to get the value 3 from "foo" (which doesn't exist), 
  then it will return "bar" becuase the key 1 is the closest
  value to 3
- When we want to create a new value using set, because we 
  are using a hashmap it allows us to do this in O(1), because
  we add every new value to the end of the key's list.
  
  but the 
  whole logic is O(log n).

"""
class TimeMap:
    def __init__(self):
        # Initialize your data structure here.
        # key : list of [val, timestamp]
        self.keyStore = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if key exists
        if key not in self.keyStore:
            # create key & empty list if not exist
            self.keyStore[key] = []    
        # add values to new key list
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # empty string for null result
        result = ""
        # find all values from hashmap or return empty list
        values = self.keyStore.get(key, [])
        # create L & R pointers
        left_pointer = 0
        right_pointer = len(values) - 1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            # [mid][1] = timestamp from values list (hashmap)
            # if timestamp in hashmap is lower/equal to timestamp given
            if values[mid][1] <= timestamp:
                # change the result to value of timestamp
                result = values[mid][0]
                # update L pointer to value next from mid
                left_pointer = mid + 1
            else:
                # move the R pointer if timestamp in hashmap is higher
                right_pointer = mid - 1
        
        return result
