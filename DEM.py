# DEM - Daily Expense Manager
import pandas as pd
from datetime import datetime

MoneyDeposited = 5000

# Date Format - (dd-mm-yyyy).
date_format = "%d-%m-%Y"

# Load an Excel file
df = pd.read_excel('DEM.xlsx', index_col=False)
mainCategory = list(df["Categories"])

# Get the current date
current_date = datetime.now()
# Format the date as mm-yyyy
formatted_date = current_date.strftime("%b-%Y")

def getAmount(prompt):
    try:
        amount = float(input(prompt))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return getAmount(prompt)
    
def getDate(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return getDate(prompt,allow_default)

def getCategory():
    while True:
        ask = input("Enter which Category expense do you wanna add (1-23): ")
        if ask.isdigit():
            ask = int(ask)
            if 1 <= ask <= 23:
                break
            else:
                print(f"Input must be between (1-23) only.")
        else:
            print("Please Enter a number.")
    return ask
    
def showCategories():
    for i,category in enumerate(df['Categories']):
        print(f"{i+1}) {category}")

# 1
def addExpense():
    showCategories()
    Category = getCategory()
    amount = getAmount(f"Enter the amount you wanna add in {mainCategory[Category-1]}: ")
    df.loc[df["SrNO."] == Category, formatted_date] += amount
    print(df)
    df.to_excel("DEM.xlsx", index=False)
    
# 2
def ViewExpense():
    try:
        month = int(input("Enter the Number of month you wanna see the Expense (1 - 12): "))
    except ValueError as e:
        print(e)
        ViewExpense()
    # Ensure the month is valid
    if 1 <= month <= 12:
        # Get the current year
        current_year = datetime.now().year

        # Create a date object with the given month and current year
        date = datetime(year=current_year, month=month, day=1)

        # Format the date as Mon-YYYY
        formatDate = date.strftime("%b-%Y")
        print("Formatted date:", formatDate)
    else:
        print("Invalid month. Please enter a value between 1 and 12.")

    TotalExpense = df[formatDate].sum()
    print(df[['Categories',formatDate]])
    print(f"The Total Expense of {formatDate} is: {TotalExpense}")
    print(f"The Total Money left in Your Acc is: {MoneyDeposited - TotalExpense}")
    
# 3
def addLendedMoney():
    df1 = pd.read_csv('DEMLended.csv', index_col=False)
    Name = input("Enter the Name of the Person: ").title().strip()
    Money = getAmount(f"Enter the amount you wanna add in Acc of {Name}: ")
    showCategories()
    Category = getCategory()
    getdate = getDate("Enter the date in (dd-mm-yyyy) or Press 'Enter' for todays date: ", allow_default=True)
    new_row = pd.DataFrame({'Name': [Name], 'Money': [Money], 'Category': [mainCategory[Category-1]], 'Date': [getdate]})

    # Append the new row using pd.concat
    try:
        df1 = pd.concat([df1, new_row], ignore_index=True)
    except FutureWarning:
        print("-------------------")
        
    print(new_row)
    df1 = df1.to_csv('DEMLended.csv', index=False)
    
# 4
def viewLendedMoney():
    df2 = pd.read_csv('DEMLended.csv', index_col=False)
    print(df2)
    
# 5
def returnMoney():
    df3 = pd.read_csv('DEMLended.csv', index_col=False)
    print(df3)
    while True:
        Name = input("Enter the Name of the Person: ").title().strip()
        if Name in list(df3["Name"]):
            break
        
    showCategories()
    while True:
        Category = getCategory()
        # s -> Total money in Excel sheet corresponding the category.
        s = df[df['Categories'] == mainCategory[Category-1]][formatted_date].sum()
        # t -> Total money in csv file corresponding to the Name and category.
        t = df3[(df3['Category'] == mainCategory[Category-1]) & (df3["Name"] == Name)]['Money'].sum()
        
        if t!=0 and s>t:
            money = input(f"Enter the Amount {Name} returned: ")
            if not money:
                df.loc[df['Categories'] == mainCategory[Category-1], formatted_date] = s - t
                df3 = df3.loc[(df3['Category'] != mainCategory[Category-1]) & (df3['Name'] != Name)]
                # Delete the specific row where Name is "Mehlam" and Category is "Dining out"
                df3 = df3.drop(df3[(df3["Name"] == Name) & (df3["Category"] == mainCategory[Category-1])])
                
            else:
                try:
                    money = float(money)
                except ValueError as e:
                    print(e)
                    
                df.loc[df['Categories'] == mainCategory[Category-1], formatted_date] = s - money
                df3.loc[(df3["Name"] == Name) & (df3["Category"] == mainCategory[Category-1]), "Money"] = t - money
                if (t-money) <= 0:
                    df3 = df3.drop(df3[(df3["Name"] == Name) & (df3["Category"] == mainCategory[Category-1])])
                
            print(df3)
            df3.to_csv('DEMLended.csv',index=False)
            df.to_excel('DEM.xlsx', index=False)
            break
                
        else:
            print("Incorrect Category Please select the correct one!")

if __name__ == '__main__':
    while True:
        print("--------------------")
        print("1. Add Expense.")
        print("2. View Expense.")
        print("3. Add Lended Money.")
        print("4. View Lended Money.")
        print("5. Returned Money")
        print("6. Exit")
        print("--------------------")

        start = input("Enter the Number (1-6): ").strip()
        if start == "1":
            addExpense()
        elif start == "2":
            ViewExpense()
        elif start == "3":
            addLendedMoney()
        elif start == "4":
            viewLendedMoney()
        elif start == "5":
            returnMoney()
        elif start == '6':
            exit()