from array import *

# Create an array and traverse
arr1 = array("i", [1, 2, 3, 4, 5, 6])
for i in arr1:
    print(i)

# Access individual elements
print(arr1[0])

# Append
arr1.append(7)
print(arr1)

# Insert
arr1.insert(0, 8)
print(arr1)

# Extend
arr1.extend([9, 10, 11])
print(arr1)

# From List
arr1.fromlist([12, 13])
print(arr1)

# Remove
arr1.remove(8)
print(arr1)

# Pop
arr1.pop()
print(arr1)

# Index
print(arr1.index(10))

# Reverse
arr1.reverse()
print(arr1)

# Buffer Info
print(arr1.buffer_info())

# Count
print(arr1.count(2))

# To String
print(arr1.tobytes())

# To List
print(arr1.tolist())

# Slice
print(arr1[1:5])
