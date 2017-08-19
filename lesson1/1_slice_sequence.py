"""
    Basic way to slice a list is somelist[start:end] where start is inclusive and end is exclusive

    The results of slicing list is a whole new list
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[:4])  # First four
print(a[-4:])  # Last four
print(a[3:-3])  # [4,5]

print(a[5:])  # 5 to end
print(a[5:len(a)])

print(a[:])  # copy
print(a[:-1])  # don't include last item

# You could use it for tuple assignments

b, c = a[:2]
print(b, c)  # 1, 2

# b, c = a[:3] will fail, because it cannot unpack

# Slice assignment

a[0:3] = [97, 98, 99]
print(a)  # [97, 98, 99, 4, 5, 6, 7, 8]

print(id(a))  # address in memory
