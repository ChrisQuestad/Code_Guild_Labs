numbers = input('Enter a number.: ')
num_int = list(map(int, numbers))

def num_sum(num_int):
    number = sum(num_int)
    return number

def check(number):
    number_str = str(number)
    return len(number_str) > 1

def num_sum_1(number):
    num_int2 = list(map(int, str(number)))
    result = sum(num_int2)
    return result

while True:
    number = num_sum(num_int)
    if check(number):
        result = num_sum_1(number)
        print(result)
    else:
        print(number)
    exit()
