import itertools as it

users = ('Mike', 'Joe', 'Bill', 'Thomas', 'Naomi', 'Emily')  # A tuple of users

def shift_maker(iterator, num_of_shifts):
    users_per_shift = len(iterator) / num_of_shifts  # Calculating the number of users per shift
    # Returning combinations of users for each shift based on the user_per_shift count
    return it.combinations(iterator, int(users_per_shift))

print(list(shift_maker(users, num_of_shifts=3)))  # Printing the list of user combinations for 3 shifts