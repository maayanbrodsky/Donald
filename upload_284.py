from typing import Dict, List

PATH = r'C:\Users\maaya\Dropbox\Python\upload_284 - Donald\accounts.txt'

def parse_file(path: str) -> Dict[int, int]:
    with open(path, 'r') as file:
        accounts: List[str] = file.readlines()
    cleaned_accounts = [account.rstrip('\r\n') for account in accounts]
    formatted_accounts = {}
    for i, account in enumerate(cleaned_accounts):
        if account[0] == '+':
           formatted_accounts[i] = int(account[1:])
        if account[0] == '-':
           formatted_accounts[i] = int(account[1:]) * - 1
    return formatted_accounts


def very_rich(accounts: Dict[int, int]):



accounts = parse_file(PATH)
