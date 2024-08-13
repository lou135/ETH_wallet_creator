from mnemonic import Mnemonic
from eth_account import Account

def create_mnemonic():
    mnemo=Mnemonic("english")
    mnemonic=mnemo.generate(strength=128)
    return mnemonic
def mnemonic_to_privatekey(mnemonic_phrase):
    Account.enable_unaudited_hdwallet_features()
    acct=Account.from_mnemonic(mnemonic_phrase,account_path="m/44'/60'/0'/0/0")
    return acct.key.hex()
def privatekey_to_address(private_key):
    acct = Account.from_key(private_key)
    address = acct.address
    return address

mnemonic=create_mnemonic()
private_key=mnemonic_to_privatekey(mnemonic)
address=privatekey_to_address(private_key)

print(f'''
Mnemonic:     {mnemonic}
Private_key:  {private_key}
Address:      {address}
''')
