# Create a text file named data.txt and write your name into it
file = open("data.txt", "w") #open this namefile and w is function to write our data
file.write("ankita,hello python world") #here u can add/write our data
file.close() #here store or save permantly data

file = open("data.txt","r") #r means read data or see output
print(file.read())
file.close()   #when u want to see output inside the file then simply open file using read function

# Open an existing file in read mode and display its contents.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# Write a program to write 5 lines into a file.
file = open("lines.txt", "w")
file.write("hello my name is tanvi\n")
file.write("i am a good girl\n")
file.write("i am learning python\n")
file.write("file handling is easy\n")
file.write("this is my fifth line\n")
file.close()

file = open("lines.txt","r") #r means read data or see output
print(file.read())
file.close() 


# Implement a simple login system using file handling.
# 1st step is create file then read
with open("users.txt", "w") as file:
    file.write("anuja,1234\n")
    file.write("rahul,abcd\n")

username = input("Enter username: ")
password = input("Enter password: ")

login_success = False

with open("users.txt", "r") as file:
    for line in file: #chk one line at an time 
        stored_username, stored_password = line.strip().split(",")

        if username == stored_username and password == stored_password:
            login_success = True
            break

if login_success:
    print("Login successful")
else:
    print("Invalid username or password")


# Create a Library Management System storing book details in a file.
# Logic 
"""Add Book → a mode
View Books → r mode
Search Book → r mode + loop
Menu Driven → while loop"""

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    price = input("Enter Price: ")

    with open("books.txt", "a") as file:
        file.write(book_id + "," + name + "," + author + "," + price + "\n")

    print("Book added successfully")


def view_books():
    try:
        with open("books.txt", "r") as file:
            print("\nBookID | Book Name | Author | Price")
            print("----------------------------------")
            for line in file:
                book_id, name, author, price = line.strip().split(",")
                print(book_id, "|", name, "|", author, "|", price)
    except FileNotFoundError:
        print("No records found")


def search_book():
    search_name = input("Enter book name to search: ")
    found = False

    try:
        with open("books.txt", "r") as file:
            for line in file:
                book_id, name, author, price = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print("Book Found:")
                    print("ID:", book_id)
                    print("Name:", name)
                    print("Author:", author)
                    print("Price:", price)
                    found = True
                    break
        if not found:
            print("Book not found")
    except FileNotFoundError:
        print("File does not exist")


while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
