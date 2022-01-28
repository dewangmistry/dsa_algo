# Python implementation of Queue using deque

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        """
        Add to queue
        """
        self.buffer.appendleft(val)

    def dequeue(self):
        """
        Remove from queue
        """
        if self.size() == 0:
            return
        return self.buffer.pop()

    def is_empty(self) -> bool:
        """
        Check if queue is empty
        """
        return len(self.buffer) == 0

    def size(self) -> int:
        """
        Return size of queue
        """
        return len(self.buffer)

if __name__ == "__main__":
    q = Queue()
    print(q.size())

    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })

    q.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    print(q.size())
    print(q.dequeue())
