class BankAccound:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def __repr__(self) -> str:
        return f'{self.name}: {self.balance}'


accout_1 = BankAccound('Junior', 1000)
accout_2 = BankAccound('Personal', 4000)
accout_3 = BankAccound('Brokers', 5000)
accout_4 = BankAccound('Savings', 7500)
accout_5 = BankAccound('Retirement', 10000)


def account_manager():
    list_of_accounts = accout_1, accout_2, accout_3, accout_4, accout_5
    print(list_of_accounts)
    filtered_list = list(filter(lambda account: account.balance > 4500, list_of_accounts))
    print(f'Accounts with balance greaer than 4500: {filtered_list}\n')
    max_account = max(list_of_accounts, key=lambda account: account.balance)
    print(f'Account with the greatest bilans: {max_account}')
