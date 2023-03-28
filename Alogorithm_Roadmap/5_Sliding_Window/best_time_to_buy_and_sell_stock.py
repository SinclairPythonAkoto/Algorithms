"""Best Time To Buy And Sell Stock

LEETCODE: 121
COMPANY:  Google

You are given an array prices where prices[i] is the price of a 
given stock on the ith day.

You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that 
stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0

Solution
- You ned to find out which day is the lowest in the price list,
  then find the the highest value after that.  We then subtract 
  the lowest value from the highest value to return our profit.
- As in the example above, how would we create a logic to make
  sure we get the correct max value, even if a higher number
  is found in an index before? To do this we use our 2 pointers.
  
  L = buy
  R = sell

- We can use Two Pointers to iterate through each index value
  and compare which pointer is the highest.
- We compare the value from the first day to the second day, 
  making the L = 7 and R = 1.  If L >= R we buy our stock
  and move the L+1, along with R+1 so we can compare the next
  two days.

  prices = [ 7, 1, 5, 3, 6, 4]
             L  R                 7 > 1 = buy 1

  prices = [ 7, 1, 5, 3, 6, 4]
                L  R              1 < 5 = 5 - 1 = 4 = current_profit

- We create an object to store the current profit. After we 
  have stored our current profit, now when we checking the 
  difference between our L & R pointers, and then check to see
  if the result is higher than the current profit. 
- If it isn't, we continue checking the other pointers. If the 
  result is higher, we update the current profit to the reuslt.
- The logic continues until the list is empty and returns our maximum profit.
  
  prices = [ 7, 1, 5, 3, 6, 4]
                L     R           1 < 3 = 3 - 1 = 2 

  prices = [ 7, 1, 5, 3, 6, 4]
                L        R        1 < 6 = 6 - 1 = 6 max_profit

  prices = [ 7, 1, 5, 3, 6, 4]
                L           R     1 < 4 = 4 - 1 = 3
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialise pointers & result
        left_pointer = 0
        right_pointer = 1
        max_profit = 0

        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                # calculate profit 
                profit = prices[right_pointer] - prices[left_pointer]
                # update max profit
                max_profit = max(max_profit, profit)
            else:
                # if L > R
                # move L pointer to position of R
                left_pointer = right_pointer
            # move R by 1
            right_pointer += 1
        
        return max_profit
    



answer: Solution = Solution()

example1: List[int] = [7,1,5,3,6,4]
print(answer.maxProfit(example1))    # 5

example2: List[int] = [7,6,4,3,1]
print(answer.maxProfit(example2))    # 0
