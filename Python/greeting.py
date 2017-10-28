name = input ("Hello! What's your name?: ")
num = input("How old are you?: ")
num2 = int(num) + 1

print('*' * len('name') + name + '*' * len('name'))
print("{}, you will be {} in one year! ".format(name, num2))
