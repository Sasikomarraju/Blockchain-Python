blockchain = []


def get_last_blockchain_value():
    # This method gets the last element of the list.
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    # This method appends a new element to the list.

    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def display_values():
    # print(blockchain)
    for block in blockchain:
        print("Block is: ", block)


def get_transaction_amount():
    return float(input("Please enter the amount to add to the blockchain"))


def get_user_choice():
    user_input = input("Your Choice: ")
    return user_input


def print_static_ui_elements():
    print("Please choose from the below")
    print("1: Add a new transaction")
    print("2: Print the blocks in the blockchain")
    print("q: Quit the program")


# named arguments
# These are valid. Commented to demonstrate the usage
# add_value(transaction_amount=2.3, last_transaction=[1])
# add_value(transaction_amount=4.7, last_transaction=get_last_blockchain_value())
# add_value(transaction_amount=8, last_transaction=get_last_blockchain_value())

# get the input from the user
# txn_amount = get_transaction_amount()
# dd_value(transaction_amount=txn_amount)


def print_invalid_message():
    print("The input entered is not correct. Please select a different option")


while True:
    print_static_ui_elements()
    user_choice = get_user_choice()
    if user_choice == '1':
        txn_amount = get_transaction_amount()
        add_value(transaction_amount=txn_amount, last_transaction=get_last_blockchain_value())
    elif user_choice == '2':
        display_values()
    elif user_choice == 'q':
        break
    else:
        print_invalid_message()
