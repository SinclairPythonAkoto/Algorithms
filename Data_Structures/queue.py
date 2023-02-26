"""Queue

A queue is a data structure that allows adding elements at one end (rear),
and removing elements at the other end (front), line a line of people
waiting for a bus.

This queue implementation could be used in a real-world scenario to manage a 
printer's queue of print jobs. As each print job is submitted, it is added to 
the queue using the enqueue method. When the printer is ready to print a new job, 
it dequeues the first job in the queue using the dequeue method and prints it. 
The queue ensures that print jobs are printed in the order they were received.
"""
class PrintQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self) -> str:
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None


#  create a new print queue
printer_queue: PrintQueue = PrintQueue()

#  enqueue a print job
printer_queue.enqueue('document1.pdf')
printer_queue.enqueue('document2.pdf')

# dequeue the first print job
print_job: str = printer_queue.dequeue()
print(f'Printing: {print_job}')

# add a third print job
printer_queue.enqueue("document3.pdf")

while len(printer_queue.queue) > 0:
    print_job = printer_queue.dequeue()
    print('Printing:', print_job)

# Output
# Printing: document1.pdf
# Printing: document2.pdf
# Printing: document3.pdf
