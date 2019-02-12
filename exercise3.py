# define the function
def is_even(my_number):
    isEven = True if my_number % 2 == 0 else False
    return isEven

# test it out
print(is_even(2)) # True
print(is_even(1)) # False
print(is_even(0)) # True
print(is_even(-5)) # False
print(is_even(-6)) # True
print(is_even(0.3)) # False
print(is_even(-0.6)) # False
