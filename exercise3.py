# define the function
def is_even(my_number):
    if my_number % 2 == 0:
        return True
    else:
        return False

# test it out
print(is_even(2)) # True
print(is_even(1)) # False
print(is_even(0)) # True
print(is_even(-5)) # False
print(is_even(-6)) # True
print(is_even(0.3)) # False
print(is_even(-0.6)) # False
