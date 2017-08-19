"""
somelist[start:end:stride]  - stride is the intervel
"""

a = ["red", "blue", "green", "orange"]

print(a[::2])  # ['red', 'green']

print(a[1::2])  # ['blue', 'orange']

# Reverse  by taking negative stride

print(a[::-1])  # Reverse  by taking negative stride. Note this doesn't work well in non-unicode characters

"""
    Try to use strides without using start and end index, so that it is easy to read and then slice
    
    Slicing and Striding will create an extra shallow copy of the data. So the first operation must
    make the list as small as possible.
    
"""

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = a[::2]
c = b[1::-1]

print(a, b, c)  # ['a', 'b', 'c', 'd', 'e', 'f'] ['a', 'c', 'e'] ['c', 'a']
