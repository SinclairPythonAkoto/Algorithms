# Intuition
To solve this we can use a hashmap and the **Bucket Sort** algorithm. We create a hashmap to count how many times each number has appeared in the list.  Because this hashmap is a dictionary object, we itereate through both key-value pairs and add each value to create a list object (used to keep track of the size of the original list).  From the list object we can loop through (starting frm the end) and return our `k` answer.

# Approach
1. Create a hashmap that will count each number in the list. The key-value pairs will be the list_index:index_count.  We will also create a list to map the length of our given list.  *This is important because we can use this to retrieve our answer in the end.*
```
count: dict = {}
freq: List[List[int]] = [[] for index in range(len(nums) + 1)]
```
2. Now we loop through our list, and we update our `count` key with the iterator.  The value for the key will be the number of times we have found the number in the list.  To do this correctly, we add `1` to `count.get(val, 0)`. What this does is adds 1 to the current value from the `count` hashmap.  If the number in the hashmap doesn't exist, it means that we are entering a new key-value pair. The `0` means that if none exists, we compute 1 + 0.
```
for val in nums:
    # returns list int (key) : count int (value)
    count[val] = 1 + count.get(val, 0)
```
We can look at how this would look like under the hood:
```
# how count is being looped:
{1: 1}
{1: 2}
{1: 3}
{1: 3, 2: 1}
{1: 3, 2: 2}
{1: 3, 2: 2, 3: 1}
```
3. Now what we want to do is add each value to the hashmap to `freq` list. To do this correctly we have to loop through both key-value items and append each dictionary value to the `freq` list (by matching the item's index).
```
for index,item in count.items():
    freq[item].append(index)
```
Again we can look at how this loop works under the hood:
```
# The loop will add each time the number
# appears in its list index.
[[], [], [], [1], [], [], []]
[[], [], [2], [1], [], [], []]
[[], [3], [2], [1], [], [], []]
```
4. We can now create a list object which we will use to keep our results.
```
res: List[int] = []
```
5. We create a for-loop that starts at the end of the `freq` list, and ends at the beginning.  This range does what we need it to do; the key thing is we take the length of the `freq` list and subtract it by 1 (this marks where to start the range), then we set our ending pointer and the direction we want it to follow.
```
for index in range(len(freq) - 1, 0, -1):
```
6. We will now loop through each element of the `freq` list and add each one to the results list `res`.
```
for index in range(len(freq) - 1, 0, -1):
    for number_count in freq[index]:
        res.append(number_count)
```
7. We now need to provide a check to stop the loop when we have reached the limit of `k`.  We check if the length of the results list is equal to the number provided for the `k` value.  If it is, we stop adding values to the results list and return the array.
```
for number_count in freq[index]:
    res.append(number_count)
    if len(res) == k:
    return res
```

# Code
```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     # create hashmap to count each time number occurs in list
    count: dict = {}
    # create the array the same size as input list
    freq = [[] for index in range(len(nums) + 1)]

    # add matching iterator count to hashmap
    for val in nums:
        # list int (key) : count int (value)
        count[val] = 1 + count.get(val, 0)
    for index,item in count.items():
        freq[item].append(index)

    res: List[int] = []

    # set range end to start, going backwards, reversed order (going backwards)
    for index in range(len(freq) - 1, 0, -1):
        # add values from freq object to results list
        for number_count in freq[index]:
            res.append(number_count)
            # check if the length of results match the value of k
            if len(res) == k:
                return res   


answer: Solution = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(answer.topKFrequent(nums, k))    # [1, 2]
```