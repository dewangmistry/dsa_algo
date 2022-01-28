"""
Design a food ordering system where your python program will run two threads,

    Place Order: This thread will be placing an order and inserting that into a queue. 
                 This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
    Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
                 This thread serves an order every 2 seconds. Also start this thread 1 second after place order 
                 thread is started.

"""

from queue import Queue
import time
import threading

class FoodOrder:
    def __init__(self) -> None:
        self.order_queue = Queue()

    def place_order(self, orders):
        for order in orders:
            self.order_queue.enqueue(order)
            print(f"Placing order {order}")
            time.sleep(0.5)

    def serve_order(self):
        time.sleep(1)
        while not self.order_queue.is_empty():
            print(f"Serving order {self.order_queue.dequeue()}")
            time.sleep(2)

if __name__ == "__main__":
    fd = FoodOrder()
    t1 = threading.Thread(target=fd.place_order, args=(['pizza','samosa','pasta','biryani','burger'], ))
    t2 = threading.Thread(target=fd.serve_order)

    t1.start()
    t2.start()