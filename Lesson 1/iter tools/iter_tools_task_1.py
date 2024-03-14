import itertools as it
import time

# Define a string of characters to be used as a loading indicator.
chars = "\|/"

# Use itertools.cycle to create an infinite iterator cycling through the chars.
indicator = it.cycle(chars)

# Loop 100 times to display the loading indicator.
for _ in range(100):
    # Print the next character from the indicator, overwriting the same line.
    print(next(indicator), end='\r')
    # Pause for 0.1 seconds before printing the next character.
    time.sleep(0.1)