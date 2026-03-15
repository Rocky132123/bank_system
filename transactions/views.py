from django.shortcuts import render
from decimal import Decimal
from accounts.models import Account
from transactions.models import Transaction
from transactions.services import transfer_money, deposit_money, withdraw_money


def transfer_view(request):
    message = ""

    if request.method == "POST":
        from_acc_no = request.POST["from_account"]
        to_acc_no = request.POST["to_account"]
        amount = Decimal(request.POST["amount"])

        try:
            sender = Account.objects.get(account_number=from_acc_no)
            receiver = Account.objects.get(account_number=to_acc_no)
            transfer_money(sender.id, receiver.id, amount)
            message = "Transfer successful"
        except Account.DoesNotExist:
            message = "Account not found"
        except ValueError as e:
            message = str(e)

    return render(request, "transfer.html", {"message": message})


def deposit_view(request):
    message = ""

    if request.method == "POST":
        acc_no = request.POST["account"]
        amount = Decimal(request.POST["amount"])

        try:
            account = Account.objects.get(account_number=acc_no)
            deposit_money(account.id, amount)
            message = "Deposit successful"
        except Account.DoesNotExist:
            message = "Account not found"
        except ValueError as e:
            message = str(e)

    return render(request, "deposit.html", {"message": message})


def withdraw_view(request):
    message = ""

    if request.method == "POST":
        acc_no = request.POST["account"]
        amount = Decimal(request.POST["amount"])

        try:
            account = Account.objects.get(account_number=acc_no)
            withdraw_money(account.id, amount)
            message = "Withdrawal successful"
        except Account.DoesNotExist:
            message = "Account not found"
        except ValueError as e:
            message = str(e)

    return render(request, "withdraw.html", {"message": message})


def transactions_list(request):
    transactions = Transaction.objects.all().order_by('-id')
    return render(request, "transactions.html", {"transactions": transactions})