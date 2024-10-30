import time

class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f'We have following books in our library {self.name}')
        for book in self.booklist:
            print(book)

    def lendbooks(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender Book Database has been updated. You can take the book now")
        else:
            print(f"Book has been already been taken by {self.lendDict[book]}")

    def addbooks(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        try:
            if book not in self.lendDict:
                print("This book is not found!!")
            else:
                self.lendDict.pop(book)
                print(f"The book {book} has been has been returned!")
        except KeyError:
            print("Sorry Book not found!")

if __name__ == '__main__':
    taha = Library(['Python',
                    'Rich Dad Poor Dad',
                    'Harry Potter',
                    'Physics Part 1',
                    'Physics Part 2'],
                    "Taha's Books Library")
    
    while True:
        print(f"Welcome to the {taha.name}. Enter Your choice to continue")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Show Lend dict")

        user_choice = input("Enter your choice: ")
        
        if user_choice not in ['1','2','3','4','5']:
            print("Please, Enter a valid choice!!")
            continue
        elif user_choice == '1':
            taha.displaybooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            if book not in taha.booklist:
                print("There are no such books in the Library!")
            else:
                user = input("Enter your name: ")
                taha.lendbooks(user, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            taha.addbooks(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            taha.returnbook(book)
        elif user_choice == '5':
            for user, book in taha.lendDict.items():
                print(user,':',book)
                time.sleep(0.30)
        else:
            print("Not a valid option!")

        print("Press q to quit and c to continue")
        user_choice2 = " "
        while user_choice2!='c' and user_choice != 'q':
            user_choice2 = input('Enter (q or c): ')
            if user_choice2 == 'q':
                print("Good Bye!!")
                exit()
            elif user_choice2 == 'c':
                print("----------------------")
                continue