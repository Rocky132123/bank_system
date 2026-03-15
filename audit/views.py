from django.shortcuts import render

# Create your views here.
from audit.models import AuditLog

def audit_logs(request):

    logs = AuditLog.objects.all()

    return render(request,"audit.html",{
        "logs":logs
    })