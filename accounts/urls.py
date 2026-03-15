from django.urls import path
from .views import dashboard, accounts_list, create_account

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", accounts_list, name="accounts_list"),
    path("create-account/", create_account, name="create_account"),
]