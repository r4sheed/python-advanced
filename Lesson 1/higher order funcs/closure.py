from functools import reduce

def pow_make(n):
    """
        Calculates pow of 'n' and returns a function.

        pow_make is a higher-order function that takes an integer 'n' and returns
        another function, pow, which raises its input to the power of 'n'. This allows
        for creating custom power functions on the fly.

        :param n: The exponent to be used in the power operation.
        :return: A function that raises its input to the power of 'n'.
    """
    def pow(x):
            # The inner function that calculates x raised to the power of n.
            return x ** n

    return pow

# Using the pow_make function to create a new function that squares any given number
pow_of_2 = pow_make(2)
print(pow_of_2(2))  # Prints 4, since 2^2 = 4


numbers = [1, 2, 3, 5, 6, 7, 8, 9]
# Using the map function to apply 'pow_of_2' (square operation) to each element in 'numbers'
li = list(map(pow_of_2, numbers))
print(li)  # Prints the square of each number in the list 'numbers'.

# Filtering to apply 'pow_of_2' only to the even numbers in the list 'numbers'.
# This is done by first filtering 'numbers' to get only even numbers.
li = list(
        map(pow_of_2,
            filter(lambda x: x % 2 == 0, numbers)))
print(li)  # Prints the square of each even number in the list 'numbers'.

# Summing up the values in 'li' which contains squared values of even numbers from 'numbers'.
# This is done using the reduce function, which applies a rolling computation (in this case addition) to sequential pairs of values in 'li'.
result = reduce(lambda x, y: x + y, li)
print(result)  # Prints the sum of squared even numbers from the original list 'numbers'.