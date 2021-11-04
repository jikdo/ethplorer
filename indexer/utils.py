# Utility functions to process block data

from .models import Account

def get_account_type(account_hash, web3_provider):
    result = bool(web3_provider.eth.get_code(account_hash))
    if (result):
        return 'contract'
    else:
        return 'eoa'

def create_account(hash, web3_provider):
    """
    Creates a blockchain account. 
    
    If an account exists, it returns the account.

    Parameters
    ----------
    hash : int
         Account address
    web3_provider: obj
         A web3 provider generated from a Web3 instance
    
    Returns 
    -------
    obj 
        Account
    """

    try:
        return Account.objects.get(hash=hash)
    except Account.DoesNotExist:
        return Account.objects.create(
            hash=hash,
            account_type=get_account_type(hash, web3_provider)
        )
