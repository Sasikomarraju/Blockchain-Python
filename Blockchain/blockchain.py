import functools

MINING_REWARD = 10
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


def verify_transaction(transaction):
    # sender_balance = get_balances(transaction['sender'])
    # return sender_balance >= transaction['amount']

    return get_balances(transaction['sender']) >= transaction['amount']


def verify_transactions():
    # is_valid = False
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else
    #         is_valid = False
    # return is_valid

    # The above code can be achieve using one liner - list comprehension
    return all([verify_transaction(tx) for tx in open_transactions])


# def add_value(transaction_amount, last_transaction=[1]):
def add_transaction(recipient, sender=owner, amount=1.0):
    # This method appends a new element to the list.
    #
    # if last_transaction is None:
    #     last_transaction = [1]
    # blockchain.append([last_transaction, transaction_amount])

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    # This is list comprehension
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    # open_transactions.append(reward_transaction)
    block = {'previous_hash': hashed_block
        , 'index': len(blockchain)
        , 'transactions': copied_transactions
             }

    blockchain.append(block)
    return True


def display_values():
    # for block in open_transactions:
    #     print("Block is: ", block)
    # print(open_transactions)
    print(blockchain)


def get_balances(participant):
    # Get the amounts of all the transactions sent by a given participant in the blockchain transaction
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]

    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)

    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                   tx_sender, 0)

    # Get the amounts of all the transactions received by a given participant in the blockchain transaction
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in
                    blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
                                       tx_recipient, 0)

    # return sum_amounts(tx_recipient) - sum_amounts(tx_sender)
    return amount_received - amount_sent


def sum_amounts(transaction):
    sum_amount = 0
    for tx in transaction:
        if len(tx) > 0:
            sum_amount += tx[0]
    return sum_amount


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
    print("5: Check transaction validity")
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
        if add_transaction(recipient, amount=amount):
            print("Transaction Added")
        else:
            print("Transaction Failed")
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        display_values()
    elif user_choice == '4':
        print("Participants:", participants)
    elif user_choice == '5':
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': ''
                , 'index': 0
                , 'transactions': [{'sender': 'Sasi', 'recipient': "Sasi", 'amount': 30.0}]
                             }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print_invalid_message()

    if not verify_chain():
        print("!!!Blockchain Compromised!!! Exiting now!")
        break

    print("Balance for {} is  {:6.2f}".format('Sasi', get_balances('Sasi')))
else:
    print("User Left")
