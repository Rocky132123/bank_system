from django.db import models
from customers.models import Customer
from branches.models import Branch

class Account(models.Model):

    ACCOUNT_TYPES = [
        ("savings","Savings"),
        ("current","Current"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    balance = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_number