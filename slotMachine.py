import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 50000000

ROWS = 3
COLS = 3

symbol_count = {
    "A":3,
    "B":4,
    "C":6,
    "D":8,
}

symbol_values = {
    "A":8,
    "B":6,
    "C":4,
    "D":3,
}

def check_winnings(columns: list, lines: int, bet: int, values: dict):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows: int, cols: int, symbols: dict):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns: list):
    print("-------------")
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row])
    print("-------------")

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please Enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Select lines between (1-{MAX_LINES}) only.")
        else:
            print("Please Enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between (${MIN_BET} - ${MAX_BET}) only.")
        else:
            print("Please Enter a number.")
    return amount

def get_spin(balance: int):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You don't have much balance left. Bet accordingly!\nCurrent balance = ${balance}")
            ask_player = input("Do you want to add more amount?\n('a' for add or Enter to skip): ").lower()
            if ask_player == "a":
                while True:
                    ask_amount = input("What would you like to deposit? $")
                    if ask_amount.isdigit():
                        ask_amount = int(ask_amount)
                        if ask_amount > 0:
                            break
                        else:
                            print("Amount must be greater than 0.")
                    else:
                        print("Please Enter a number.")
                balance += ask_amount
                print(f"Current balance = ${balance}")
                
    print(f"You are betting ${bet} on {lines} lines. Your total bet = ${total_bet}")

    slots = get_slot_machine_spin(COLS,ROWS,symbol_count)
    print_slot_machine(slots)

    winning, winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"You won ${winning}")
    if len(winning_lines) == 0:
        print("You won on lines. None")
    else:
        print("You won on lines.",*winning_lines)
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press Enter to spin (q to Quit): ").lower()
        if spin == "q":
            break
        balance += get_spin(balance)

    print(f"You left with ${balance}")
            
if __name__ == "__main__": 
    ask = input("Press Enter to play (q to Quit): ").lower()
    if ask == "q":
        quit()
    else:   
            main()