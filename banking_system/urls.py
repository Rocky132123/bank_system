from django.contrib import admin
from django.urls import path

from accounts.views import dashboard, accounts_list, create_account
from transactions.views import transfer_view, deposit_view, withdraw_view, transactions_list
from loans.views import loan_list
from audit.views import audit_logs
from users.views import login_view, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Dashboard
    path("dashboard/", dashboard, name="dashboard"),

    # Accounts
    path("accounts/", accounts_list, name="accounts_list"),
    path("create-account/", create_account, name="create_account"),

    # Transactions
    path("transfer/", transfer_view, name="transfer"),
    path("deposit/", deposit_view, name="deposit"),
    path("withdraw/", withdraw_view, name="withdraw"),
    path("transactions/", transactions_list, name="transactions_list"),

    # Loans
    path("loans/", loan_list, name="loans_list"),

    # Audit
    path("audit/", audit_logs, name="audit_logs"),

    # Profile (users app has no profile view yet — using login_view as placeholder)
    path("profile/", login_view, name="profile"),
]