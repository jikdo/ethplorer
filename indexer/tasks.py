from django.db.utils import Error
from celery import shared_task
from celery.utils.log import get_task_logger
from web3 import Web3
import traceback

from django.conf import settings
from .utils import (
    get_account_type
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
            block_response = w3.eth.get_block(start_block)

            miner = Account.objects.create(
                hash=block_response.miner,
                account_type=get_account_type(block_response.miner, w3)
            )

            # block = Block.objects.create(

            # )

        except Exception as e:
            traceback.print_exception(e)
            logger.info('error happend here')
            pass

        break
