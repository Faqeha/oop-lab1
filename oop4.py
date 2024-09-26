#Qno1:

class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        
        self.title = title 
        self.author = author  
        self.publication_year = publication_year  

    def __str__(self) -> str:
        
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

if __name__ == "__main__":
    
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

    
    print(my_book)  
