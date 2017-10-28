"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

a = 'music'
b = [17, 28, 42, 31, 12]
def display_indexes(a):
    for index, le in enumerate(a):
        print(le, index)
display_indexes(a)

def parallel(a, b):
    for let, (le, num) in enumerate(zip(a, b)):
        print(le, num)

parallel(a, b)
