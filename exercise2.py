# define the negative function
def negative(my_number):
    isNegative = True if my_number < 0 else False
    return isNegative

# test it out
print(negative(-1))
print(negative(1))
print(negative(-0.5))
print(negative(0.5))
print(negative(0))
