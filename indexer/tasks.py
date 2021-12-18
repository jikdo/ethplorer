
from datetime import datetime
import time
import traceback

from django.utils import timezone
from celery import shared_task
from celery.utils.log import get_task_logger
from web3 import Web3
from web3.exceptions import BlockNotFound

from django.conf import settings
from .utils import (
    get_account_type,
    create_account,
)

from .models import (
    Block, Transaction,
    Account
)

logger = get_task_logger(__name__)


@shared_task
def index_blockchain(start_block_id):
    logger.info('lets work')
    # initialize web3
    provider = Web3.HTTPProvider(settings.WEB3_PROVIDER)
    w3 = Web3(provider)

    # fetch blockchain data
    start_block = start_block_id
    current_block_number = w3.eth.block_number
    if (start_block > current_block_number):
        logger.info(
            f'Error: start_block must be <= current block height - {current_block_number}')
        return 'Invalid block number'

    while(True):

        try:

            logger.info(f'something is happening: block {start_block}')

            block_response = w3.eth.get_block(
                start_block, full_transactions=True)

            miner = Account.objects.create(
                hash=block_response.miner,
                account_type=get_account_type(block_response.miner, w3)
            )

            def get_parent_block(number):
                try:
                    Block.objects.get(number=number)
                except Block.DoesNotExist:
                    return None

            block = Block.objects.create(
                hash=Web3.toHex(block_response.hash),
                parent_block=None if block_response.number == 0 else get_parent_block(
                    block_response.number - 1),
                difficulty=block_response.difficulty,
                extra_data=block_response.extraData,
                gas_limit=block_response.gasLimit,
                gas_used=block_response.gasUsed,
                logs_bloom=block_response.logsBloom,
                miner=miner,
                nonce=Web3.toHex(block_response.nonce),
                number=block_response.number,
                receipt_root=Web3.toHex(block_response.receiptsRoot),
                sha3_uncles=Web3.toHex(block_response.sha3Uncles),
                size=block_response.size,
                state_root=Web3.toHex(block_response.stateRoot),
                timestamp=timezone.make_aware(
                    datetime.fromtimestamp(block_response.timestamp)),
                total_difficulty=block_response.totalDifficulty,
                transactions_root=Web3.toHex(block_response.transactionsRoot),
                transaction_count=w3.eth.get_block_transaction_count(
                    block_response.number)
            )

            # save transactions
            for tx in block_response.transactions:
            
                Transaction.objects.create(
                    block=block,
                    from_address=create_account(tx['from'], w3),
                    gas=tx.gas,
                    gas_price=tx.gasPrice,
                    hash=Web3.toHex(tx.hash),
                    input=tx.input,
                    # max_fee_per_gas=tx.maxFeePerGas,
                    # max_priority_fee_per_gas=tx.maxPriorityFeePerGas,
                    nonce=tx.nonce,
                    to_address=create_account(tx.to, w3),
                    transaction_index=tx.transactionIndex,
                    value=tx.value,
                )

            # go to next block
            start_block += 1

        # wait for 15 mins
        except BlockNotFound:
            print('Block not found')

            # wait for new block (blocktime for ethereum is around 13s )
            print('Waiting for next block ..')
            time.sleep(20)
        except Exception as e:
            traceback.print_exc()
            break
