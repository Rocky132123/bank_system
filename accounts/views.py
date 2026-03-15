from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from customers.models import Customer
from branches.models import Branch
from transactions.models import Transaction


@login_required
def dashboard(request):
    accounts = Account.objects.all()
    transactions = Transaction.objects.all()[:5]
    total_balance = sum(a.balance for a in accounts)

    return render(request, "dashboard.html", {
        "accounts": accounts,
        "transactions": transactions,
        "total_balance": total_balance,
    })


def accounts_list(request):
    accounts = Account.objects.all()
    return render(request, "accounts.html", {
        "accounts": accounts,
    })


def create_account(request):
    if request.method == "POST":
        account_number = request.POST["account_number"]
        account_type = request.POST["account_type"]
        balance = request.POST["balance"]
        customer_id = request.POST["customer"]
        branch_id = request.POST["branch"]

        customer = Customer.objects.get(id=customer_id)
        branch = Branch.objects.get(id=branch_id)

        Account.objects.create(
            account_number=account_number,
            account_type=account_type,
            balance=balance,
            customer=customer,
            branch=branch,
        )
        return redirect("/accounts/")

    customers = Customer.objects.all()
    branches = Branch.objects.all()
    return render(request, "create_account.html", {
        "customers": customers,
        "branches": branches,
    })