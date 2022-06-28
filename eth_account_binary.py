from eth_account import Account

Account.enable_unaudited_hdwallet_features()

new_eth_account, mnemonic = Account.create_with_mnemonic()

pub_address = new_eth_account.address
private_key = new_eth_account.key.hex()
mnemonic_phrase = mnemonic

print(f"Public address: {pub_address}, Private key: {private_key}, Mnemonic phrase: {mnemonic_phrase}")
