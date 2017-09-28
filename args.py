"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""
def arb(*args):
    number = len(args)
    print('The {} args are: {}'.format(number, args))



def stats(*args):
    num_sum = sum(args)
    print('Sum: {}'.format(num_sum))
    num_max = max(args)
    print('Max: {}'.format(num_max))
    num_min = min(args)
    print('Min: {}'.format(num_min))
    num_avg = int(num_sum / len(args))
    print('Avg: {}' .format(num_avg))
    num_range = num_max - num_min
    print('Range: {}' .format(num_range))
    num_entries = len(args)
    print('Entries: {}' .format(num_entries))
