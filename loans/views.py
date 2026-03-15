from django.shortcuts import render

# Create your views here.
from loans.models import Loan

def loan_list(request):

    loans = Loan.objects.all()

    return render(request,"loan.html",{
        "loans":loans
    })
