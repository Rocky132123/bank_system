from django.db import models
from accounts.models import Account


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ('transfer', 'Transfer'),
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    from_account = models.ForeignKey(
        Account,
        related_name="sent_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True  # nullable for deposits (no sender)
    )
    to_account = models.ForeignKey(
        Account,
        related_name="received_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True  # nullable for withdrawals (no receiver)
    )

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - ₹{self.amount}"