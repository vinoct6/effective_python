"""
In Python you could add an else block after a loop

"""

for i in range(3):
    print(i)
else:
    print('Else Block!!')

"""
0
1
2
Else Block!!

The else block ran soon after the for loop
but if you add a break statement, else won't happen
"""

for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print('Else Block!!')


# Runs in the both the cases below

for i in []:
    print("never runs")
else:
    print("runs")

while False:
    print("never runs")
else:
    print("runs")


try:
    raise Exception('Doh!')
    print('Will not be reached')
except:
    print('Caught exception')

try:
    x = 3 + 5
finally:
    print('This always runs')
