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
    number = models.IntegerField()
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






class Transaction:
    """
    Represents a transaction on the ethereum blockchian
    """
    pass
