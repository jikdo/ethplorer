from django.contrib import admin
from .models import (
    Account,
    Block,
    Transaction
)

# Register your models here.
admin.site.register(Block)
admin.site.register(Account)
admin.site.register(Transaction)