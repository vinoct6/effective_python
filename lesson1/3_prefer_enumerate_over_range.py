from random import randint

"""
    range is useful in loops

"""

for i in range(64):
    print(i)

random_bits = 0

for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i

"""Iterate directly over lists"""

flavor_list = ['vanilla', 'chocolate', 'pecan']

for flavor in flavor_list:
    print('%s is delicious' % flavor)

# You could do index too
# This example doesn't look good.. hard to read..extra noise
for i in range(0, len(flavor_list)):
    flavor = flavor_list[i]
    print("%d : %s" % (i, flavor))

# Enumerate wraps iterator with lazy generator
flavor_list = ['vanilla', 'chocolate', 'pecan']
print(list(enumerate(flavor_list))) # [(0, 'vanilla'), (1, 'chocolate'), (2, 'pecan')]

for i, flavor in enumerate(flavor_list, 1):  # 1 specifies where to start counting
    print("%d : %s" % (i, flavor))



