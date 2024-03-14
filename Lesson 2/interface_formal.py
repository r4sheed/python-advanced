""" The abc module in Python provides infrastructure for defining custom abstract base classes (ABCs).
Abstract base classes are a form of interface checking more strict than individual hasattr()
checks for particular methods. By defining an abstract base class, you can define a common
API for a set of subclasses. This capability is especially useful in situations where a
third-party is going to provide implementations, such as with plugins, but can also aid
you in working with your own code. An abstract method is one that is declared in the abstract
class, but it may not provide any implementation. Subclasses are expected to implement these
methods. The abc module provides the functionality to define these abstract methods using
the @abstractmethod decorator. """

import abc

import abc

class Bird(abc.ABC):
    # Define an abstract base class Bird using the ABC module
    @abc.abstractmethod
    def fly(self):
        # This method is declared but not implemented,
        # indicating subclasses are required to provide their own implementation
        pass

class Parrot(Bird):
    # Parrot is a subclass of Bird and provides an implementation of the fly method
    def fly(self):
        print('Flying')

parrot = Parrot() # Create an instance of Parrot

class Plane(abc.ABC):
    # Define an abstract base class Plane using the ABC module
    @abc.abstractmethod
    def fly(self):
        # This method is declared but not implemented,
        # indicating subclasses are required to provide their own implementation
        pass

class Boeing(Plane):
    # Boeing is a subclass of Plane and provides an implementation of the fly method
    def fly(self):
        print('Flying')

boeing = Boeing() # Create an instance of Boeing
boeing.fly() # Calls the `fly` method on the `boeing` instance, which is an instance of the Boeing class that implements the fly method from the Plane abstract base class. Prints 'Flying'.

print(isinstance(parrot, Bird)) # Check if parrot is an instance of Bird -> True
print(isinstance(parrot, Plane)) # Check if parrot is an instance of Plane -> False

print(isinstance(boeing, Plane)) # Check if boeing is an instance of Plane -> True
print(isinstance(boeing, Bird)) # Check if boeing is an instance of Bird -> False
