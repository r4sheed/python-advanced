import itertools as it
import random

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['♠', '♦', '♣', '♥']

# Generate a deck of cards as a sequence of tuples, combining each rank with each suit.
def cards():
    """ Return a generator that yields playing cards. """
    for rank in ranks:
        for suit in suits:
            yield rank, suit

# Create a deck of cards using a generator expression for more concise code.
cards = ((rank, suit) for rank in ranks for suit in suits)
# Example: list(cards) would return a list of tuples representing a deck of cards without jokers.
print()

# Itertools are useful for creating and manipulating iterators in efficient ways.
# Examples:

# - it.product for creating Cartesian products of iterables.
# Example: Cartesian product of two lists
list1 = [1, 2]
list2 = ['a', 'b']
product = it.product(list1, list2)

# Convert the iterator to a list to print the results
print(list(product)) # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# - it.tee for splitting an iterator into multiple independent iterators.
# Example: Splitting an iterator into two
numbers = iter(range(5))
iter1, iter2 = it.tee(numbers)

# Consume the first iterator
print(next(iter1)) # Output: 0
print(next(iter1)) # Output: 1

# Consume the second iterator
print(next(iter2)) # Output: 0
print(next(iter2)) # Output: 1

# - it.islice for slicing iterators.
# Example: Slicing an iterator
numbers = iter(range(10))
sliced = it.islice(numbers, 2, 5)

# Convert the iterator to a list to print the results
print(list(sliced)) # Output: [2, 3, 4]

# - it.chain for chaining multiple iterators together.
# Example: Chaining multiple iterators
iter1 = iter([1, 2, 3])
iter2 = iter([4, 5, 6])
chained = it.chain(iter1, iter2)

# Convert the iterator to a list to print the results
print(list(chained)) # Output: [1, 2, 3, 4, 5, 6]

# Create a deck of cards using itertools.product to achieve the same as above, but in an even more concise way.
cards = it.product(ranks, suits)
# Example: list(cards) generates the same list of card tuples as the generator expression.
print()

def shuffle(cards):
    """ Return iterator over a shuffled deck. """
    deck = list(cards)
    random.shuffle(deck)  # Shuffle the deck randomly.
    return iter(tuple(deck))  # Return an iterator over the shuffled deck.

cards = shuffle(cards)  # Shuffle the initial deck of cards created with itertools.
# Example: list(cards) now returns a randomly shuffled list of card tuples.
# print()

def cut(deck, n):
    """ Return an iterator over a deck of cards cut at index `n`. """
    if n < 0:  # Ensure n is non-negative.
        raise ValueError('`n` must be a non-negative integer')

    deck = list(deck)  # Convert the iterable deck into a list for slicing.
    return iter(deck[n:] + deck[:n])  # Perform the cut and return an iterator over the result.

cards = cut(cards, 26)  # Cut the deck in the middle.
# Example: list(cards) shows the deck after being cut in the middle.
# print()

def cut(deck, n):
    """ Return an iterator over a deck of cards cut at index `n`. """
    # Using itertools for efficient slicing and concatenating
    deck1, deck2 = it.tee(deck, 2)  # Duplicate the deck into two iterators.
    top = it.islice(deck1, n)       # Get the top n cards.
    bottom = it.islice(deck2, n, None)  # Get the bottom cards from n to the end.
    return it.chain(top, bottom)    # Concatenate the top and bottom parts.

cards = cut(cards, 26)  # Perform the cut operation using itertools.
# Example: list(cards) now shows the deck after a more efficient cut operation.
# print()

def deal(deck, num_hands=3, hand_size=5):
    iters = [iter(deck)] * hand_size  # Prepare iterators for dealing.
    print(iters)
    hands_gen = (tuple(it.islice(itr, num_hands)) for itr in iters)  # Generate hands from iterators.
    return zip(*(tuple(hands_gen)))  # Zip the generated hands into tuples representing each hand.

hand_1, hand_2, hand_3 = deal(cards, num_hands=3)  # Deal 3 hands of 5 cards each.
# Example: Printing hand_1, hand_2, and hand_3 will show the cards dealt to each hand.
print(hand_1, hand_2, hand_3)