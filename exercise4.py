# define the function
def eightCharsOrLonger(my_string):
    return len(my_string) >= 8

# test it out
print(eightCharsOrLonger("abcdefg")) # False
print(eightCharsOrLonger("abcdefgh")) # True
print(eightCharsOrLonger("abcdefghi")) # True
print(eightCharsOrLonger("a")) # False
print(eightCharsOrLonger("")) # False
print(eightCharsOrLonger("        ")) # True
print(eightCharsOrLonger("abcdefg ")) # True
