def make_is_div(n):
     # This function creates and returns another function, is_div_n,
     # that checks if a number is divisible by 'n'
     def is_div_n(x):
          # Returns True if 'x' is divisible by 'n', otherwise False
          return x % n == 0
     return is_div_n

# Create a list of functions that check divisibility for numbers 1 to 10000
divisibles = [make_is_div(n) for n in range(1, 10001)]

for i, div in enumerate(divisibles, start=1):
     # For each divisibility checking function, test if 23423453 is divisible
     # 'i' represents the divisor (from 1 to 10000), 'div' is the function
     if (div(23423453)):
          # If 23423453 is divisible by 'i', print 'i'
          print(i, end=',')

# Print a newline character at the end of the output
print()