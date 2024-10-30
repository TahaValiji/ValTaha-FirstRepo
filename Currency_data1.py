with open("Currency1.csv","r") as file:
    lines = file.readlines()
    currency_list = []
    for line in lines:
        parsed = line.split(", ")
        currency_list.append(parsed)

with open("Currency.csv","a") as file:
    for i,lists in enumerate(currency_list):
        writer = file.write(f"{i+1},{lists[0]},{lists[1]},{lists[2]}")