from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSACTION_TYPE 

# Create your models here.
class Transactions(models.Model):
    account=models.ForeignKey(UserBankAccount,related_name='transactions',on_delete=models.CASCADE)

    amount=models.DecimalField(max_digits=12,decimal_places=2)
    balance_after_transaction=models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approve=models.BooleanField(default=False)
    receiver_account = models.IntegerField(default=1)

    class Meta:
        ordering=['timestamp']

class Bank(models.Model):
    name = models.CharField(max_length=200,default='bankrupt',null=True,blank=True)
    is_bankrupt = models.BooleanField(default=False)




