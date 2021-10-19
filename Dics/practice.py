a = {}
a[1, 2] = 1
a[(1, 2)] = 2
print(a)
b = a.copy()
print(id(a))
print(id(b))

my_dict = {}
my_dict[1] = 1
my_dict["1"] = 2
my_dict[1.0] = 4

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(my_dict)
