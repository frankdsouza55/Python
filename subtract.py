# Problem statement: https://edabit.com/challenge/7eQNpraoWR3JxZMKB

# Recursive approach
def my_sub(x, y):
    # returns y-x
    if y == 0:
        return x
    return my_sub(x ^ y, (~x & y) << 1)


# Iterative approach
# def my_sub(x, y):
#     while(y != 0):
#         borrow = (~x & y)
#         x = x ^ y
#         y = borrow << 1
#     return x


# Driver Code
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x < y:
    x, y = y, x
diff = my_sub(x, y)
print("Difference = " + str(diff))
