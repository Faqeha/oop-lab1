#Qno1:

# Class:
# A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
# Classes encapsulate data for the object and the methods to manipulate that data.

# Object:
# An object is an instance of a class. It is created based on the structure defined by the class.
# Objects contain actual values and can call the methods defined in the class.

#example

class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)


print(my_dog.name)       
print(my_dog.age)        
print(my_dog.bark())     


#Qno2:
# Constructor Method (__init__):

# The __init__ method is a special method in Python used to initialize newly created objects. It is called automatically when an object of a class is instantiated.
# This method can take parameters that allow you to set initial values for the object's attributes.

# __str__() Method:

# The __str__() method is another special method that defines a human-readable string representation of an object. It is called when you use the print() function or the str() function on an object.
# This method is helpful for providing a clear and understandable output when an object is printed, allowing users to see its state in a meaningful way.


    
