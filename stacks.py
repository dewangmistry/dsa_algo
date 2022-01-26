# Python implementation of Stacks using dequeue

from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        """
        Push value to stack
        """
        self.container.append(val)
        return

    def pop(self):
        """
        Pop value from stack
        """
        return self.container.pop()
    
    def peek(self):
        """
        Return top element from stack
        """
        return self.container[-1]

    def is_empty(self):
        """
        Check if stack is empty and return boolean value
        """
        return len(self.container) == 0

    def size(self):
        """
        return size of stack
        """
        return len(self.container)

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    s.push(2)
    s.push(3)
    s.push(5)
    s.push(6)
    print(s.peek())
    # print(s)

