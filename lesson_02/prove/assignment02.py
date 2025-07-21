"""
Course    : CSE 351
Assignment: 02
Student   : <your name here>

Instructions:
    - review instructions in the course
"""

# Don't import any other packages for this assignment
import os
import random
import threading
from money import *
from cse351 import *

# ---------------------------------------------------------------------------
def main(): 

    print('\nATM Processing Program:')
    print('=======================\n')

    create_data_files_if_needed()

    # Load ATM data files
    data_files = get_filenames('data_files')
    # print(data_files)
    # with open('data_files\\atm-01.dat', 'r') as file:
    #     lines = file.readlines()
    # print(lines[1].split(',')[1])
    
    
    log = Log(show_terminal=True)
    log.start_timer()

    bank = Bank()

    # TODO - Add a ATM_Reader for each data file
    threads = []
    for data in data_files:
        # print(data)
        t = ATM_Reader(data, bank)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    test_balances(bank)

    log.stop_timer('Total time')


# ===========================================================================
class ATM_Reader(threading.Thread):
    # TODO - implement this class here
    def __init__(self, data_file, bank):
        threading.Thread.__init__(self)
        self.data_file = data_file
        self.bank = bank

    def run(self):
        # print(self.data_file)
        with open(self.data_file, 'r') as file:
            lines = file.readlines()
        for line in lines[2:]:
            account = line.split(',')[0]
            type = line.split(',')[1]
            amount = line.split(',')[2]
            if type == 'w':
                self.bank.withdraw(account, amount)
            elif type == 'd':
                self.bank.deposit(account, amount)
        
        
    ...


# ===========================================================================
class Account():
    # TODO - implement this class here
    # money
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        value = Money(amount.strip())
        # print(self.balance)
        value2 = Money(str(self.balance))
        # self.balance = value.add(self.balance)
        self.balance = float(amount.strip()) + float(self.balance)
        


    def withdraw(self, amount):
        self.balance = float(self.balance) - float(amount.strip()) 

    def get_balance(self):
        pass
        # return money
    ...


# ===========================================================================
class Bank():
    # TODO - implement this class here
    accountstupples = (
        (1, '0'),
        (2, '0'),
        (3, '0'),
        (4, '0'),
        (5, '0'),
        (6, '0'),
        (7, '0'),
        (8, '0'),
        (9, '0'),
        (10, '0'),
        (11, '0'),
        (12, '0'),
        (13, '0'),
        (14, '0'),
        (15, '0'),
        (16, '0'),
        (17, '0'),
        (18, '0'),
        (19, '0'),
        (20, '0'),
    )
    global accounts
    accounts = dict(accountstupples)
    global lock 
    lock = threading.Lock()

    def __init__(self):
        self.accounts = accounts

    def deposit(self, account_number, amount):
        lock.acquire()
        try:
            account_number = int(account_number)
            account = Account(self.accounts[account_number])
            account.deposit(str(amount))
            self.accounts[account_number] = account.balance
        finally:
            lock.release()
        # print(account)
        # balance = accounts[account_number]
        # amount = amount.split()
        # total = float(balance) + float(amount[0])
        # # print(total)
        # total = str(total)
        # # print(account_number, ":", accounts[account_number])
        # accounts[account_number] = total
        # # print(account_number, ":", accounts[account_number])
        

    def withdraw(self, account_number, amount):
        lock.acquire()
        try:
            account_number = int(account_number)
            account = Account(self.accounts[account_number])
            account.withdraw(str(amount))
            self.accounts[account_number] = account.balance
        finally:
            lock.release()
        # account_number = int(account_number)
        # balance = accounts[account_number]
        # amount = amount.split()
        # total = float(balance) - float(amount[0])
        # # print(total)
        # total = str(total)
        # accounts[account_number] = total
        # print(account_number, ":", accounts[account_number], "\n")
        

    def get_balance(self, account_number):
        account_number = int(account_number)
        # print("accounts", accounts[account_number])
        amount = str("{:.2f}".format(self.accounts[account_number]))
        # amount = "{:.2f}".format(amount)
        return Money(amount)

# ---------------------------------------------------------------------------

def get_filenames(folder):
    """ Don't Change """
    filenames = []
    for filename in os.listdir(folder):
        if filename.endswith(".dat"):
            filenames.append(os.path.join(folder, filename))
    return filenames

# ---------------------------------------------------------------------------
def create_data_files_if_needed():
    """ Don't Change """
    ATMS = 10
    ACCOUNTS = 20
    TRANSACTIONS = 250000

    sub_dir = 'data_files'
    if os.path.exists(sub_dir):
        return

    print('Creating Data Files: (Only runs once)')
    os.makedirs(sub_dir)

    random.seed(102030)
    mean = 100.00
    std_dev = 50.00

    for atm in range(1, ATMS + 1):
        filename = f'{sub_dir}/atm-{atm:02d}.dat'
        print(f'- {filename}')
        with open(filename, 'w') as f:
            f.write(f'# Atm transactions from machine {atm:02d}\n')
            f.write('# format: account number, type, amount\n')

            # create random transactions
            for i in range(TRANSACTIONS):
                account = random.randint(1, ACCOUNTS)
                trans_type = 'd' if random.randint(0, 1) == 0 else 'w'
                amount = f'{(random.gauss(mean, std_dev)):0.2f}'
                f.write(f'{account},{trans_type},{amount}\n')

    print()

# ---------------------------------------------------------------------------
def test_balances(bank):
    """ Don't Change """

    # Verify balances for each account
    correct_results = (
        (1, '59362.93'),
        (2, '11988.60'),
        (3, '35982.34'),
        (4, '-22474.29'),
        (5, '11998.99'),
        (6, '-42110.72'),
        (7, '-3038.78'),
        (8, '18118.83'),
        (9, '35529.50'),
        (10, '2722.01'),
        (11, '11194.88'),
        (12, '-37512.97'),
        (13, '-21252.47'),
        (14, '41287.06'),
        (15, '7766.52'),
        (16, '-26820.11'),
        (17, '15792.78'),
        (18, '-12626.83'),
        (19, '-59303.54'),
        (20, '-47460.38'),
    )

    wrong = False
    for account_number, balance in correct_results:
        # print(account_number)
        bal = bank.get_balance(account_number)
        print(f'{account_number:02d}: balance = {bal}')
        if Money(balance) != bal:
            wrong = True
            print(f'Wrong Balance: account = {account_number}, expected = {balance}, actual = {bal}')

    if not wrong:
        print('\nAll account balances are correct')



if __name__ == "__main__":
    main()

