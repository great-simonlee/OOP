from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, 'SeunghoonLeeOne'))
pq.put((1, 'SeunghoonLeeTwo'))

popped_element = pq.get()

print("Popped Element:", popped_element[1])
print("Remaining Queue:")
while not pq.empty():
    print(pq.get()[1])