# define the wrapping function
def wrap_text(my_string, wrap):
    new_string = wrap + my_string + wrap
    return new_string

# one wrap
print(wrap_text('hello', '==='))
# three wraps
wraps = ["###", "===", "---"]
final_string = 'hello'
for wrap in wraps:
    final_string = wrap_text(final_string, wrap)
print(final_string)
