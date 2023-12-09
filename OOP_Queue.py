from queue import Queue

q = Queue()

q.put('SeunghoonLeeOne')
q.put('SeunghoonLeeTwo')

popped_element = q.get()

print("Popped Element:", popped_element)
print("Remaining Queue:", list(q.queue))

