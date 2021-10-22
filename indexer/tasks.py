from celery import shared_task
from .models import (
    Block, Transaction,
    Account
)

@shared_task
def index_blockchain(block_height):
    pass