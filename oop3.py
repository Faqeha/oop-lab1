#Qno1:
class Rectangle:
    def __init__(self, width: float, height: float):
    
        self.width = width  
        self.height = height  

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        
        return f"Rectangle(Width: {self.width}, Height: {self.height})"


rect = Rectangle(5.0, 3.0)

print(rect)  
print(f"Area: {rect.area()}") 
print(f"Perimeter: {rect.perimeter()}")  

#Qno2:

class Rectangle:
    def __init__(self, width: float, height: float):
        
        self.width = width  
        self.height = height  

    def __str__(self) -> str:
    
        return f"Rectangle: {self.width} x {self.height}"

    def area(self) -> float:
        
        return self.width * self.height

    def perimeter(self) -> float:
        
        return 2 * (self.width + self.height)


rect = Rectangle(5.0, 3.0)

print(rect)  
print(f"Area: {rect.area()}")  
print(f"Perimeter: {rect.perimeter()}")  

#Qno3:

class Rectangle:
    def __init__(self, width: float, height: float):
       
        self.width = width  # Attribute: width
        self.height = height  # Attribute: height

    def __str__(self) -> str:
        
        return f"Rectangle: {self.width} x {self.height}"

    def area(self) -> float:
        
        return self.width * self.height

    def perimeter(self) -> float:
        
        return 2 * (self.width + self.height)

def main():
    
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    rect = Rectangle(width, height)
    print(rect)

    
    print(f"Area: {rect.area()}")

    print(f"Perimeter: {rect.perimeter()}")

if __name__ == "__main__":
    main()


