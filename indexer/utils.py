# Utility functions to process block data

def get_account_type(account_hash, web3_provider):
    result = bool(web3_provider.eth.get_code(account_hash))
    if (result):
        return 'contract'
    else:
        return 'eoa'
