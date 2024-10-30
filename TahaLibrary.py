import pandas as pd
from datetime import datetime
import time

date_format = "%d-%m-%Y"

def get_name():
    name = input("Enter your name: ").lower().title()   
    return name

def get_date(prompt: str, allow_default: bool = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def addBook():
    with open("Books.csv","a",newline="") as file:
        bookName = input("Enter the name of Book you wanna add: ").lower().title()
        writer = input("Enter the author's name: ").lower().title()
        file.write(f"{bookName},{writer}\n")

def Books():
    with open("Books.csv","r") as file:
        lines = file.readlines()
        BookList = []
        for i,line in enumerate(lines):
            if i != 0:
                parsed = line.split(",")
                BookList.append(parsed[0])
    return BookList

def displayBooks():
    print("------------------------")
    BookList = Books()
    print("We have following books in out library:")
    for i,book in enumerate(sorted(BookList)):
        print(f"{i+1}) {book}")
    print("------------------------")

def lended_books():
    with open("Lend_Book.csv","r") as file:
        lines = file.readlines()
        LendedBookList = []
        for i,line in enumerate(lines):
            if i != 0:
                parsed = line.split(",")
                LendedBookDict = {}
                LendedBookDict["BookName"] = parsed[0]
                LendedBookDict["Name"] = parsed[1]
                LendedBookDict["Date"] = parsed[2].replace("\n","")
                LendedBookList.append(LendedBookDict)
    return LendedBookList

def lendBook():
    BookList = Books()
    with open("Lend_Book.csv","a",newline="") as file:
        LendedBookList = lended_books()
        while True:
            askBook = input("Enter the name of Book you wanna Lend: ").lower().title()
            if checkBook(LendedBookList, askBook):
                for book in LendedBookList:
                    if askBook == str(book['BookName']):
                        print(f"{askBook} is already lended to {book['Name']}. Please try another one.\n")
                continue

            if askBook in BookList:
                name = get_name()
                prompt = input("Enter the date in (dd-mm-yyyy) format or Tap Enter for todays date: ")
                date = get_date(prompt, allow_default = True)
                file.write(f"{askBook},{name},{date}\n")
                print(f"{askBook} Lended to {name} Successfully!")
                break
            else:
                print(f"{askBook} is Not-Available now.")

def checkBook(LendedBookList, askBook):
    for book in LendedBookList:
        if askBook == str(book['BookName']):
            return True
    return False

def display_lended_books():
    print("------------------------")
    LendedBookList = lended_books()
    print("We have following books lended:")
    for i,book in enumerate(LendedBookList):
        print(f'{i+1}) {book["BookName"]} - {book["Name"]} - {book["Date"]}')
    print("------------------------")

def returnBook():
    LendedBookList = lended_books()
    display_lended_books()
    ask_book = input("Enter The name of book You are returning: ").lower().title()
    for book in LendedBookList:
        if ask_book == str(book['BookName']):
            name = get_name()
            if name == str(book['Name']):
                df = pd.read_csv("Lend_Book.csv")
                df = df[df['BookName'] != ask_book]
                df.to_csv("Lend_Book.csv", index=False)
                print(f"{name} has returned {ask_book} successfully.")
                main()
            else:
                print(f"{name} has not lended {ask_book}.\n")
                returnBook()
    else:
        print(f"Sorry! {ask_book} not Found.")

def countName():
    LendedBookList = lended_books()
    askName = input("Enter the Name: ").lower().title()
    count = 0
    countList = []
    for dict in LendedBookList:
        if askName == str(dict['Name']):
            count += 1
            countList.append(dict['BookName'])
    printList = ", ".join(countList)
    print(f"{askName} has lended {count} books.")
    if count != 0:
        print(f"{askName} has lended following books: {printList}")

def main():
    while True:
        print("....")
        time.sleep(1)
        print("Enter 1 to Add a Book")
        print("Enter 2 to Lend a Book")
        print("Enter 3 to Return a Book")
        print("Enter 4 to Display Books")
        print("Enter 5 to Display Lended Books")
        print("Enter 6 to Count Name")
        print("Enter 7 to Exit")

        choice = input("Enter Your Choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 7:
                if choice == 1:
                    addBook()
                elif choice == 2:
                    displayBooks()
                    lendBook()
                elif choice == 3:
                    returnBook()
                elif choice == 4:
                    displayBooks()
                elif choice == 5:
                    display_lended_books()
                elif choice == 6:
                    countName()
                elif choice == 7:
                    break
            else:
                print("Invalid choice. Please Enter a number between 1 and 6.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to Taha's Library")
    main()