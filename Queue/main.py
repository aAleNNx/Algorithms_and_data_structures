import circular_array as c_a

queue = c_a.queue_cir()
queue.enqueue(0)
queue.enqueue(1)
print(queue.dequeue())
print(queue.peek())
for i in range(2, 5):
    queue.enqueue(i)
print(queue.dequeue())
print(queue)
for i in range(5, 9):
    queue.enqueue(i)
print(queue)
while not queue.is_empty():
    print(queue.dequeue())
print(queue)
