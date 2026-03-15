from django.shortcuts import render

# Create your views here.
from customers.models import Customer

def profile(request):

    customers = Customer.objects.all()

    return render(request,"profile.html",{
        "customers":customers
    })