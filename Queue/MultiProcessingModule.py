from multiprocessing import Queue

custQueue = Queue(maxsize=3)
custQueue.put(0)
custQueue.put(1)
custQueue.put(2)
print(custQueue.full())
print(custQueue.empty())
print(custQueue.get())
print(custQueue.get())
