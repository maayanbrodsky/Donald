from typing import List


PATH = r'C:\Users\maaya\Dropbox\Python\upload_284 - Donald\accounts.txt'

def parse_file(path: str) -> List[int]:
    """Takes a file path, reads the txt file and returns a list
    of integers in order and according to positive or negative state."""
    with open(path, 'r') as file:
        accounts: List[str] = file.readlines()
    cleaned_accounts = [account.rstrip('\r\n') for account in accounts]
    formatted_accounts = []
    for i, account in enumerate(cleaned_accounts):
        if account[0] == '+':
           formatted_accounts.append(int(account[1:]))
        if account[0] == '-':
           formatted_accounts.append(int(account[1:]) * -1)
    return formatted_accounts


def very_rich(accounts: List[int], first_day: int, last_day: int) -> int:
    """Takes parsed data and first and last day slices the list and returns the sum."""
    return sum(accounts[first_day - 1:last_day])


accounts = parse_file(PATH)
print(accounts)
print(very_rich(accounts, 3, 6))