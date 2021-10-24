from collections import deque

custQueue = deque(maxlen=3)
print(custQueue)
custQueue.append(0)
custQueue.append(1)
custQueue.append(2)
print(custQueue)
custQueue.append(3)
print(custQueue)
print(custQueue.popleft())
print(custQueue)
custQueue.clear()
print(custQueue)
