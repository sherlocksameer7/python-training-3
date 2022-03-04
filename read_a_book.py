count_of_books = int(input("Enter the num of books? "))
book = []
# author_name = []
# book_price = []
# publisher_name = []
for i in range(0, count_of_books):
    bk_name = input("Enter the name of the book? ")
    aut_name = input("Enter the author name of the book? ")
    bk_price = int(input("Enter the price of the book? "))
    pb_name = input("Enter the publishers name? ")
    Book_details = {"Book_name": bk_name,
                    "Author_name": aut_name,
                    "Book_Price": bk_price,
                    "Publisher_name": pb_name
                    }
    book.append(Book_details)
print("Book Details in Dictionary ", book)
# print("Book Names ", book_name)
# print("Book Price ", book_price)
# print("Author Names ", author_name)
# print("Publisher Names", publisher_name)
# print()
# print(employee_age)
# print(employee_designation)
# print(employee_salary)