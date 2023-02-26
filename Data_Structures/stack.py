"""Stacks

A stack is a data structure that allows adding and removing elements
only at one end (normally the top), like a stack of plates.

One common use of a stack is in web browsers, where the back and forward 
buttons maintain a history of visited web pages. Each time a new page is 
visited, it is added to the top of the history stack. When the back button 
is clicked, the most recently visited page is popped off the stack and displayed.



The implementation below could be used in a real-world scenario to implement 
the back button functionality in a web browser. As each page is visited, it is 
added to the stack using the push method. When the back button is clicked, the 
most recently visited page is removed from the stack using the pop method, and 
the previous page is displayed. The peek method can be used to display the current 
top page on the stack without removing it.
"""
class BrowserStack:
    def __init__(self):
        self.stack = [] 

    def push(self, url: str) -> None:
        self.stack.append(url)
    
    def pop(self) -> str:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self) -> str:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


# create a new browser stack
browser_stack: BrowserStack = BrowserStack()

# visit some pages and add them to the stack
browser_stack.push('https://www.google.com')
browser_stack.push('https://www.facebook.com')
browser_stack.push('https://twitter.com')
browser_stack.push('https://www.linkedin.com')

# check the current top page on the stack
print(f'Current page: {browser_stack.peek()}')

# click back button to go back a page
previous_page = browser_stack.pop()
print(f'Previous page: {previous_page}')

# check the current top page on stack
print(f'Current page: {browser_stack.peek()}')

# click back button again to go on previous page
previous_page = browser_stack.pop()
print(f'Previous page: {previous_page}')

print(f'Current page: {browser_stack.peek()}')

# Output
# Current page: https://www.linkedin.com
# Previous page: https://www.linkedin.com
# Current page: https://twitter.com
# Previous page: https://twitter.com
# Current page: https://www.facebook.com