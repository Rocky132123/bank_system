from django.db import transaction
from accounts.models import Account
from transactions.models import Transaction


@transaction.atomic
def transfer_money(from_account_id, to_account_id, amount):
    sender = Account.objects.select_for_update().get(id=from_account_id)
    receiver = Account.objects.select_for_update().get(id=to_account_id)

    if sender.balance < amount:
        raise ValueError("Insufficient balance")

    sender.balance -= amount
    receiver.balance += amount
    sender.save()
    receiver.save()

    Transaction.objects.create(
        from_account=sender,
        to_account=receiver,
        amount=amount,
        transaction_type="transfer"
    )
    return "Transfer Successful"


@transaction.atomic
def deposit_money(account_id, amount):
    account = Account.objects.select_for_update().get(id=account_id)
    account.balance += amount
    account.save()

    Transaction.objects.create(
        from_account=None,
        to_account=account,
        amount=amount,
        transaction_type="deposit"
    )
    return "Deposit Successful"


@transaction.atomic
def withdraw_money(account_id, amount):
    account = Account.objects.select_for_update().get(id=account_id)

    if account.balance < amount:
        raise ValueError("Insufficient balance")

    account.balance -= amount
    account.save()

    Transaction.objects.create(
        from_account=account,
        to_account=None,
        amount=amount,
        transaction_type="withdrawal"
    )
    return "Withdraw Successful"