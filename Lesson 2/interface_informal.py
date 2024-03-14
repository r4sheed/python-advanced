""" Summary: Informal interfaces in Python, also known as protocols, are a set of methods that a class can implement to enable its instances to be used in a certain way. For example, classes can implement iterator protocols (__iter__ and __next__) to allow their instances to be iterated over with a for loop, container protocols (__contains__) to support the in operator, and the sized protocol (__len__) to allow len() to be called on their instances. These protocols enable Python's flexible and dynamic nature, allowing objects to interact with built-in functions and operators in a variety of ways without the need for explicit inheritance from abstract base classes. This approach promotes duck typing, where an object's suitability for a certain operation is determined by the methods it implements, rather than its class hierarchy. """

class Team:
    def __init__(self, members) -> None:
        # Initializes the Team class with a list of members
        self.__members = members
        # Initialize index to start iteration from the beginning of the members list
        self.__index = 0

    def __len__(self):
        # Implements the Sized protocol to return the number of members
        return len(self.__members)

    def __contains__(self, member):
        # Implements the Container protocol to check if a member is part of the team
        return member in self.__members

    def __iter__(self):
        self.__index = 0  # Reset index for new iteration
        # Implements the Iterator protocol to return the iterator object itself
        return self

    def __next__(self):
        # Implements the Iterator protocol to iterate through the members
        if self.__index < len(self.__members):
            member = self.__members[self.__index]
            self.__index += 1
            return member
        raise StopIteration

league = Team(['Batman', 'Wonder Woman', 'Deadpool'])

# Utilizing the Sized protocol to get the number of members in the team
print(len(league))

# Utilizing the Container protocol to check membership in the team
print('Batman' in league)
print('Wolverine' not in league)
print('Deadpool' not in league)

# Utilizing the Iterator protocol to loop through the team members
for member in league:
    print(member)