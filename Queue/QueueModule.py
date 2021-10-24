import queue as q

custQueue = q.Queue(maxsize=3)
print(custQueue.qsize())
print(custQueue.empty())
custQueue.put(0)
custQueue.put(1)
custQueue.put(2)
print(custQueue.qsize())
print(custQueue.full())
print(custQueue.get())
print(custQueue.qsize())
