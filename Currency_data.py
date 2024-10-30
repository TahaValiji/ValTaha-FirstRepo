def get_CurrencyList():
    with open("Currency.csv","r") as file:
        lines = file.readlines()
        currencyList = []
        for line in lines:
            parsed = line.split(",")
            if "\n" in parsed[3]: 
                parsed[3] = parsed[3].replace("\n","")     
            currencyList.append(parsed)
    return currencyList

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount < 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError:
        print("Invalid. Amount must be a number")
        return get_amount()
    
def get_curr_country():
    while True:
        curr_country = input("Enter the currency code: ")
        if curr_country.isdigit():
            curr_country = int(curr_country)
            if 0 < curr_country <= len(get_CurrencyList()):
                break
            else:
                print(f"Amount must be in the range of (1-{len(get_CurrencyList())})")
        else:
            print("Invalid. Enter a Positive Integer.")
    return curr_country

def choose_one():
    print("Do you want to change INR to other currency or viceversa?\n1. INR to other currency\n2. Other currency to INR")
    say = input("Choose (1 or 2): ")
    if say == "1":
        Inr_to_other()
    elif say == "2":
        other_to_inr()
    else:
        print("Invalid. Enter 1 or 2.")
        choose_one()

def choose_one1(currencyList: list):
    print("Do you want to change INR other currency or viceversa?\n1. INR to other currency\n2. Other currency to INR")
    say = input("Choose (1 or 2): ")
    if say == "1":
        after_Inr_to_other(currencyList)
    elif say == "2":
        after_Other_to_inr(currencyList)
    else:
        print("Invalid. Enter 1 or 2.")
        choose_one1(currencyList)

def after_Inr_to_other(currencyList: list):
    curr_country = get_curr_country()
    print(f"Changing INR to {currencyList[curr_country-1][1]}.  (1 INR is equal to {float(currencyList[curr_country-1][2]):.2f} {currencyList[curr_country-1][1]})")
    amount = get_amount()
    Total_value = amount * float(currencyList[curr_country-1][2])
    #Round off Total_value to 2 decimal places.
    Total_value = round(Total_value, 2)
    print(f"{amount}(INR) is equal to {Total_value}({currencyList[curr_country-1][1]})\n")
    ask = input("Do you want to use the currency converter again? (yes or no): ").lower()
    if ask == "yes":
        choose_one1(currencyList)
    else:
        print("Thankyou for using the currency converter. Goodbye!\n")
        quit()

def after_Other_to_inr(currencyList: list):
    curr_country = get_curr_country()
    print(f"Changing {currencyList[curr_country-1][1]} to INR.  (1 {currencyList[curr_country-1][1]} is equal to {float(currencyList[curr_country-1][3]):.2f} INR)")
    amount = get_amount()
    Total_value = amount * float(currencyList[curr_country-1][3])
    #Round off Total_value to 2 decimal places.
    Total_value = round(Total_value, 2)
    print(f"{amount}({currencyList[curr_country-1][1]}) is equal to {Total_value}(INR)\n")
    ask = input("Do you want to use the currency converter again? (yes or no): ").lower()
    if ask == "yes":
        choose_one1(currencyList)
    else:
        print("Thankyou for using the currency converter. Goodbye!\n")
        quit()

def Inr_to_other():
    print("\n")
    print("Welcome to Currency Converter.")
    print("List of Currencies:\n")
    currencyList = get_CurrencyList()
    for i in currencyList:
        print(f"{i[0]}. {i[1]}")
    print("\n")
    curr_country = get_curr_country()
    print(f"Changing INR to {currencyList[curr_country-1][1]}.  (1 INR is equal to {float(currencyList[curr_country-1][2]):.2f} {currencyList[curr_country-1][1]})")
    amount = get_amount()
    Total_value = amount * float(currencyList[curr_country-1][2])
    #Round off Total_value to 2 decimal places.
    Total_value = round(Total_value, 2)
    print(f"{amount}(INR) is equal to {Total_value}({currencyList[curr_country-1][1]})\n")
    ask = input("Do you want to use the currency converter again? (yes or no): ").lower()
    if ask == "yes":
        choose_one1(currencyList)
    else:
        print("Thankyou for using the currency converter. Goodbye!\n")
        quit()
    
def other_to_inr():
    print("\n")
    print("Welcome to Currency Converter.")
    print("List of Currencies:\n")
    currencyList = get_CurrencyList()
    for i in currencyList:
        print(f"{i[0]}. {i[1]}")
    print("\n")
    curr_country = get_curr_country()
    print(f"Changing {currencyList[curr_country-1][1]} to INR.  (1 {currencyList[curr_country-1][1]} is equal to {float(currencyList[curr_country-1][3]):.2f} INR)")
    amount = get_amount()
    Total_value = amount * float(currencyList[curr_country-1][3])
    #Round off Total_value to 2 decimal places.
    Total_value = round(Total_value, 2)
    print(f"{amount}({currencyList[curr_country-1][1]}) is equal to {Total_value}(INR)\n")

    ask = input("Do you want to use the currency converter again? (yes or no): ").lower()
    if ask == "yes":
        choose_one1(currencyList)
    else:
        print("Thankyou for using the currency converter. Goodbye!\n")
        quit()

def main(): 
    ask = input("Do you want to use the currency converter? (yes or no): ").lower()
    if ask == "yes":
        choose_one()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()