class MyNumbers:
    def __iter__(self):
        # Initializes the number attribute to 1 every time an iterator is created from MyNumbers instance
        self.number = 1
        return self

    def __next__(self):
        # Saves the current number to be returned
        value = self.number
        # Doubles the number for the next iteration
        self.number *= 2
        # Returns the previously saved value
        return value

# Creates an instance of MyNumbers class
my_class = MyNumbers()
# Gets an iterator from the my_class instance
my_iter = iter(my_class)

# Loops over the iterator 8 times, doubling the output each time starting from 1
for i in range(8):
    print(next(my_iter))

print()

# Defines a generator function that yields numbers and print statements
def my_gen():
    number = 1
    print('First')
    yield number  # Yields 1 and pauses execution here

    number += 1  # Resumes here when next() is called again
    print('Second')
    yield number  # Yields 2 and pauses execution here

# Creates an iterator from the generator function my_gen
my_iter = iter(my_gen())

# Attempts to get 3 values from the iterator but only 2 are available
for i in range(3):
    print(next(my_iter, 'No more elements'))  # 'No more elements' is printed when the iterator is exhausted

print()

# List of numbers
my_list = [1, 3, 5, 7, 10]

# List comprehension that calculates the square of each number in my_list
[x ** 2 for x in my_list]  # The result is a list of squared numbers

# Generator expression that does the same as above but lazily
(x ** 2 for x in my_list)  # This creates a generator object for efficient memory management, not an immediate list