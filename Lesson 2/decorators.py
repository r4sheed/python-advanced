import time

def logged(fn):
    # This decorator logs the function call with its arguments and result.
    def wrapper(*args):
        print(f'You called: {fn.__name__}({args})')  # Log the function call with arguments.
        results = fn(*args)  # Execute the decorated function.
        print(f'Result was: {results}')  # Log the result.
        return results  # Return the result of the decorated function call.
    return wrapper  # Return the wrapper function.

@logged
def try_something(*args):
    # Function to demonstrate logging of calls and results.
    print(*args)  # Print arguments.
    return 'success'  # Return a sample result.

try_something('I', 'am', 'trying', 'something')  # Example call to a logged function.

def timeit_decorator(fn):
    # This decorator measures and logs the execution time of functions.
    def wrapper(*args):
        start = time.time()  # Start time before function execution.
        res = fn(*args)  # Execute the decorated function.
        end = time.time()  # End time after function execution.
        print(f'{fn.__name__} took {(end - start) * 1000} ms')  # Log the execution time.
        return res  # Return the result of the decorated function.
    return wrapper  # Return the wrapper function.

@timeit_decorator
def comprehension():
    # Function that returns a list comprehension.
    return [x ** 2 for x in range(3_000_000)]  # Return a list of squares.

@timeit_decorator
def generator():
    # Function that returns a generator expression.
    return (x ** 2 for x in range(3_000_000))  # Return a generator of squares.

@timeit_decorator
def iter_over(iter):
    # Function to iterate over an iterable argument.
    for _ in iter:  # Iterate through the given iterable.
        pass  # Perform no action during iteration.

comp = comprehension()  # Create a list of squares and measure time.
iter_over(comp)  # Iterate through the list and measure time.

gen = generator()  # Create a generator of squares and measure time.
iter_over(gen)  # Iterate through the generator and measure time.