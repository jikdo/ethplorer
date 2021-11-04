from django.utils import timezone
from datetime import datetime

from django.db.utils import Error
from celery import shared_task
from celery.utils.log import get_task_logger
from web3 import Web3
import traceback

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
        return f'Error: start_block must be <= current block height - {current_block_number}'

    while(True):

        try:

            logger.info('something is happening')
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
                hash=block_response.hash,
                parent_block=None if block_response.number == 0 else get_parent_block(
                    block_response.number - 1),
                difficulty=block_response.difficulty,
                extra_data=block_response.extra_data,
                gas_limit=block_response.gas_limit,
                gas_used=block_response.gas_used,
                logs_bloom=block_response.logs_bloom,
                miner=miner,
                nonce=block_response.nonce,
                number=block_response.number,
                receipt_root=block_response.receipt_root,
                sha3_uncles=block_response.sha3_uncles,
                size=block_response.size,
                state_root=block_response.state_root,
                timestamp=timezone.make_aware(
                    datetime.fromtimestamp(block_response.timestamp)),
                total_difficulty=block_response.total_difficulty,
                transactions_root=block_response.transactions_root,
                transaction_count=w3.eth.get_block_transaction_count(
                    block_response.number)
            )

            # save transactions
            for tx in block_response.transactions:

                Transaction.objects.create(
                    block_hash=block,
                    from_address=create_account(tx.from_address, w3),
                    gas=tx.gas,
                    gas_price=tx.gas_price,
                    hash=tx.hash,
                    input=tx.input,
                    max_fee_per_gas=tx.max_fee_per_gas,
                    max_priority_fee_per_gas=tx.max_priority_fee_per_gas,
                    nonce=tx.nonce,
                    to_address=tx.to_address,
                    transaction_index=tx.transaction_index,
                    value=tx.value,
                )

            # go to next block
            start_block += 1

        except Exception as e:
            traceback.print_exception(e)

        break
