from django.db import models
from .custom_fields import BiggerIntegerField

# Create your models here.


class Block(models.Model):
    """
    Represents an ethereum block on the chain
    """
    hash = models.CharField(max_length=150)
    difficulty = BiggerIntegerField()
    extra_data = models.CharField(max_length=100)
    gas_limit = models.IntegerField()
    gas_used = models.IntegerField()
    logs_bloom = models.TextField()
    miner = models.CharField(max_length=42)
    nonce = models.CharField(max_length=50)
    number = models.BigIntegerField()
    parent_hash = models.CharField(max_length=150)
    receipt_root = models.CharField(max_length=150)
    sha3_uncles = models.CharField(max_length=150)
    size = models.IntegerField()
    state_root = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    total_difficulty = BiggerIntegerField()
    transactions_root = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True,
                                   help_text='Date added to off-chain database')

    def __str__(self) -> str:
        return self.hash


class Transaction(models.Model):
    """
    Represents a transaction on the ethereum blockchian
    """
    hash = models.CharField(max_length=150)
    block_hash = models.CharField(max_length=150)
    block_number = models.BigIntegerField()
    from_address = models.CharField(max_length=150)
    gas = models.BigIntegerField()
    gas_price = models.BigIntegerField()
    input = models.CharField(max_length=150)
    max_fee_per_gas = models.BigIntegerField()
    max_priority_fee_per_gas = models.BigIntegerField()
    nonce = models.IntegerField()
    to_address = models.CharField(max_length=150)
    transaction_index = models.IntegerField()
    value = models.BigIntegerField()

    def __str__(self) -> str:
        return self.hash


class Account(models.Model):
    pass


class Contract(models.Model):
    pass
