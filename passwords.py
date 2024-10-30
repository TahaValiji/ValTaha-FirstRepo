import random

def view():
    with open("password.csv","r") as r:
        lines = r.readlines()
        row_count = len(lines)
        i=1
        for line in lines:
            data = line.rstrip()
            user, passw = data.split(" | ")
            print("--------------------------------------")
            print(f"{i}) User: {user} | Password:{passw}")
            i+=1
    print("--------------------------------------")

def add():
    user = input("Enter your account username: ")
    passw = input("Do you want to write your own password or you want a random password (w or r): ")
    if passw == "w":
        my_own_pass = input("Enter your password: ")

        def add_in_file(my_own_pass):
            with open('password.csv', 'a') as file:
                file.write(user + ' | ' + my_own_pass + "\n")
                print("--------------------------------------")
                print(f"Your written password for {user} is '{my_own_pass}'")
                print("--------------------------------------")

        def tryagain():
            while True:
                my_own_pass = input("Type your Password again(must contain 8 letters): ")
                if len(my_own_pass)<8:
                    print("Password must be of 8 characters")
                    continue
                else:
                    add_in_file(my_own_pass)

        if len(my_own_pass)<8:
            print("Password must be of 8 characters")
            tryagain()
        else:
            add_in_file(my_own_pass)

    elif passw == "r":
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
        numbers = "1234567890"
        symbols = "!@#$%^&"
        length = 8
        output = lower_case + upper_case + numbers + symbols
        password = "".join(random.sample(output, length))
        with open('password.csv', 'a') as f:
            f.write(user + ' | ' + password + "\n")
            print("--------------------------------------")
            print(f"Your random password for {user} is '{password}'")
            print("--------------------------------------")
    else:
        print("Invalid Input. Try again!!")

def main():
    while True:
        mode = input("You want to add new passwords or want to view exsisting ones (view or add) or print q if you want to quit: ").lower()
        if mode == "q":
            print("Good bye!")
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid input. Try again!")
            continue

def tryagain():
    i=3
    while i!=0:
        mas_pass = input(f"You have {i} chances\nEnter the Master Password: ")
        if mas_pass == "st123":
            main()
        elif mas_pass != "st123":
            print(f"{mas_pass} is INCORRECT!")
            i-=1
            continue

if __name__=="__main__":
    master_pass = input("Enter the Master Password: ").lower()
    if master_pass == "st123":
        main()
    elif master_pass != "st123":
        print(f"{master_pass} is INCORRECT!")
        tryagain()