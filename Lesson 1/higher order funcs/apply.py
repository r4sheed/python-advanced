def apply(fn, iterable):
    # This function takes a function (fn) and an iterable, then
    # iterates over each item in the iterable, applies the function
    # to each item, and prints the result.

    for i in iterable:
        print(fn(i))  # Applies fn to each item i in iterable and prints.

words = ['Hello', 'there', 'world']  # List of words to be processed
apply(lambda s: s.upper(), words)  # Applies the lambda function to uppercase each word in words list.