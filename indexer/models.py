from django.db import models
from django.db.models.fields import related
from .custom_fields import BiggerIntegerField

# Create your models here.


class Block(models.Model):
    """
    Represents an ethereum block on the chain
    """
    hash = models.CharField(max_length=500, unique=True)
    difficulty = BiggerIntegerField()
    extra_data = models.CharField(max_length=100)
    gas_limit = models.IntegerField()
    gas_used = models.IntegerField()
    logs_bloom = models.TextField()
    miner = models.ForeignKey(
        'Account', related_name="mined_blocks", on_delete=models.CASCADE)
    nonce = models.CharField(max_length=200)
    number = models.BigIntegerField()
    parent_block = models.OneToOneField(
        'self', related_name="parent", null=True, on_delete=models.CASCADE)
    receipt_root = models.CharField(max_length=500)
    sha3_uncles = models.CharField(max_length=500)
    size = models.IntegerField()
    state_root = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    total_difficulty = BiggerIntegerField()
    transactions_root = models.CharField(max_length=500)
    transaction_count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,
                                   help_text='Date added to off-chain database')

    def __str__(self) -> str:
        return f'{self.hash} {self.timestamp}'


class Transaction(models.Model):
    """
    Represents a transaction on the ethereum blockchian
    """
    hash = models.CharField(max_length=500, unique=True)
    block = models.ForeignKey(
        Block, related_name='transactions', on_delete=models.CASCADE)
    from_address = models.ForeignKey(
        'Account', related_name='from_transactions', on_delete=models.CASCADE)
    gas = models.BigIntegerField()
    gas_price = models.BigIntegerField()
    input = models.TextField()
    # max_fee_per_gas = models.BigIntegerField()
    # max_priority_fee_per_gas = models.BigIntegerField()
    nonce = models.IntegerField()
    to_address = models.ForeignKey(
        'Account', related_name='to_transactions', on_delete=models.CASCADE)
    transaction_index = models.IntegerField()
    value = BiggerIntegerField()

    def __str__(self) -> str:
        return self.hash


class Account(models.Model):
    """
    Represents an ethereum account
    """
    ACCOUNT_TYPE_CHOICES = (
        ('eoa', 'Externally Owned Account'),
        ('contract', 'Contract'),

    )

    hash = models.CharField(max_length=42, unique=True, help_text="account address")
    account_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.hash} ({self.account_type})'
