from web3 import Web3
from datetime import datetime
import pprint


provider = Web3.HTTPProvider('https://mainnet.infura.io/v3/debda1da0c694c36a8f4a4b86fbb9144')
w3 = Web3(provider)

print(w3.eth.get_block(1000000).hash.hex())


# tx = w3.eth.get_transaction('0x2539884855adef927de3e68ed3b3feb79dfdda70383accb11f1e95ff158eedf8')
# print(tx)

print('private key')
print(bool(w3.eth.get_code('0x24354D31bC9D90F62FE5f2454709C32049cf866b')))

print('contract')
print(bool(w3.eth.get_code('0x8798249c2E607446EfB7Ad49eC89dD1865Ff4272')))