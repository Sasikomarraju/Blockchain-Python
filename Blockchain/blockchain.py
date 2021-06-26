genesis_block = {'previous_hash': ''
    , 'index': 0
    , 'transactions': []
                 }
hacker_block = {'previous_hash': ''
    , 'index': 0
    , 'transactions': [{'sender': 'Sasi', 'recipient': "Sasi", 'amount': 30.0}]
                }
participants = {'Sasi'}

blockchain = [genesis_block]
open_transactions = []
owner = "Sasi"


def get_last_blockchain_value():
    # This method gets the last element of the list.
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# def add_value(transaction_amount, last_transaction=[1]):
def add_transaction(recipient, sender=owner, amount=1.0):
    # This method appends a new element to the list.
    #
    # if last_transaction is None:
    #     last_transaction = [1]
    # blockchain.append([last_transaction, transaction_amount])

    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)

    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    # This is list comprehension
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block
        , 'index': len(blockchain)
        , 'transactions': open_transactions
             }

    blockchain.append(block)
    return True


def display_values():
    # for block in open_transactions:
    #     print("Block is: ", block)
    # print(open_transactions)
    print(blockchain)


def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_transaction_data():
    input_recipient = input('Enter the recipient of the transaction: ')
    input_amount = float(input("Please enter the amount to add to the blockchain"))
    return input_recipient, input_amount


def get_user_choice():
    user_input = input("Your Choice: ")
    return user_input


def print_static_ui_elements():
    print("Please choose from the below")
    print("1: Add a new transaction")
    print("2: Mine a new block")
    print("3: Print the blocks in the blockchain")
    print("4: Output participants")
    print("h: Manipulate")
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


def hash_block(block):
    print("Inside hAsh block", block)
    print("Inside Hash block", '-'.join([str(block[key]) for key in block]))
    return '-'.join([str(block[key]) for key in block])


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print_static_ui_elements()
    user_choice = get_user_choice()
    if user_choice == '1':
        txn_data = get_transaction_data()
        recipient, amount = txn_data
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        display_values()
    elif user_choice == '4':
        print("Participants:", participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            print("Length of blockchain", len(blockchain))
            # blockchain[0] = [hacker_block]
            blockchain[0] = {'previous_hash': ''
                , 'index': 0
                , 'transactions': [{'sender': 'Sasi', 'recipient': "Sasi", 'amount': 30.0}]
                             }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print_invalid_message()

    if not verify_chain():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!Blockchain Compromised!!!!!!!!!!!!!!!!!!! Exiting now!")
        break

    print("Balance for Sasi", get_balances('Sasi'))
else:
    print("User Left")
