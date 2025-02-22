import random


MAX_LINES = 3 # Maximum number of lines in the slot machine
MAX_BET = 100 # Maximum bet amount
MIN_BET = 1 # Minimum bet amount

ROWS = 3   # Number of rows in the slot machine
COLS = 3 # Number of columns in the slot machine

sym_list = { # List of symbols in the slot machine and their how many are in each column.
    'Bell': 6,
    'Cherry': 4,
    'Star': 2,
    'Diamond': 1 
}

sym_value = { # Multiplier for each symbol
    'Bell': 2,
    'Cherry': 3,
    'Star': 5,
    'Diamond': 10 
}


def check_winnings(columns, lines, bet,values):
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
            winning_lines.append(line + 1)

    return winnings, winning_lines
        

def get_slot_machine_spin(rows,cols,symbols): # Function to generate a random spin of the slot machine
    spins = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            spins.append(symbol)

    columns = []
    for _ in range(cols): # Generate a column for each column we have (for example, if we have 3 columns, we need to do everything in the loop 3 times.
        column = []
        current_symbols = spins[:] # current_symbols is a copy of the spin list (we need to make a copy so we can remove elements from it without affecting the original list)
        for _ in range(rows): # Generate a row for each row we have (for example, if we have 3 rows, we need to do everything in the loop 3 times.
            value = random.choice(current_symbols) # Pick a random symbol from the current_symbols list
            current_symbols.remove(value) # Remove the symbol from the current_symbols list so it can't be picked again
            column.append(value) # Add the symbol to the column
        
        columns.append(column) # Add the column to the columns list

    return columns 

def print_slot_machine(columns): # Function to print the slot machine
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") # Print the symbol in the column followed by a pipe character (|) to separate the columns
            else:
                print(column[row], end="")

        print() # Print a newline character to move to the next row100



def  deposit(): # Function to deposit money into the account (Asks the user for an amount to deposit)
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # Check if the input is a number
            amount = int(amount) # Convert the input to an integer
            if amount > 0:
                break # Breaks the loop if the input is a valid number
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")

    return amount


def get_num_lines():
    while True:
        lines = input("Enter the number of lines you would like to play (1-" + str(MAX_LINES) + ")? ") # This ensures that the user can only enter a number between 1 and the maximum number of lines.      
        if lines.isdigit(): 
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES: 
                break 
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break 
            else: 
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to make that bet, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, sym_list)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, sym_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit() 
    while True:
        print(f"Your current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"Thank you for playing! Your final balance is: ${balance}")

main()