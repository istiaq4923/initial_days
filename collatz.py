def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
        # step += 1
        # return step
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
        # step += 1
        # return step

n = input('Type an integer: ')
step = 0
try:
    while n!= 1:
        n = collatz(int(n))
except ValueError:
    print('Please enter an interger.')

# print(sum(1 for _ in collatz(n)))

# def collatz(n):
#  while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#         yield(n)
#     else:
#         n = n * 3 + 1
#         yield(n)
# n = input('Type an integer: ')
# print(len(list(collatz(int(n)))))  # More obvious what's happening
# # 17


# import time, sys
# indent = 0 # How many spaces to indent.
# indentIncreasing = True # Whether the indentation is increasing or not.
# try:
#     while True: # The main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10 of a second.
#
#         if indentIncreasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indentIncreasing = False
#
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()
