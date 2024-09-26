# Qno1:

def is_prime(number):

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(11))  
print(is_prime(10)) 

#Qno2:

import math

def is_prime(number):
    
    if number <= 1:
        return False
    if number <= 3:
        return True 
    
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  
    return True  

print(is_prime(11))  
print(is_prime(10))  
print(is_prime(17))  
print(is_prime(4))   

#Qno3:

import math

def is_prime(number):
    
    if number <= 1:
        return False
    if number <= 3:
        return True  
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  
    return True  

def main():
    while True:
        user_input = input("Enter a number to check if it is prime (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            number = int(user_input)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

#Qno4:

import math

def is_prime(number):

    if number <= 1:
        return False
    if number <= 3:
        return True  
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  
    return True  

def main():
    while True:
        user_input = input("Enter a number to check if it is prime (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            number = int(user_input)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

