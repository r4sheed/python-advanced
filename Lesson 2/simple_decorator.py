def uppercase_decorator(fn):
    def wrapper():
        # This inner function wraps the original function, modifying its output
        return fn().upper()  # Call the original function, then convert its result to uppercase
    return wrapper  # Return the wrapper function to be used as the decorator

@uppercase_decorator  # Apply the decorator to modify the behavior of `say_hi`
def say_hi():
    return 'Hi there!'  # Original function returns a greeting string

print(say_hi())
# HI THERE!