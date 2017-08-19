"""Item 4: Use Zip to process items in parallel

"""

names = ['Sachin Tendulkar', 'Rahul Dravid', 'Ganguly']
letters = [len(name) for name in names]

# To iterate over both lists(names and letters) in parallel,

for i in range(len(names)):
    count = letters[i]
    print(count)

print("________________________________________")


# In python 3 zip wraps two or more iterators with a lazy generator

print(list(zip(names, letters)))  # [('Sachin', 6), ('Dravid', 6), ('Ganguly', 7)]

print("________________________________________")


# Find the name with maximum length
name_with_max_length = ''
max_length = 0
for letter, name in zip(letters, names):
    if letter > max_length:
        max_length = len(name)
        name_with_max_length = name

print(name_with_max_length)

# Note that zip behaves strangely if the length is of different lengths
print("________________________________________")

names.append("Vinoth")

for name, count in zip(names, letters):
    print('%s has %d letters ' % (name, count))

"""

Output :

Note that 'Vinoth' did not show up at all
Sachin Tendulkar has 16 letters 
Rahul Dravid has 12 letters 
Ganguly has 7 letters 

whichever, iterators get exhausted first, it stops there
"""

# solution to this is a function called zip_longest
print("________________________________________")
from itertools import zip_longest

for name, count in zip_longest(names, letters):
    if count is None:
        print('%s is of unknown length' % name)
    else:
        print('%s has %d letters ' % (name, count))

"""
Output :
Sachin Tendulkar has 16 letters 
Rahul Dravid has 12 letters 
Ganguly has 7 letters 
Vinoth is of unknown length

"""
