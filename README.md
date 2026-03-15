# 🏦 Banking System — Django Web Application

A full-stack banking management system built with Django and PostgreSQL, featuring account management, fund transfers, loan tracking, and audit logging.

---

## 🚀 Features

- 🔐 **User Authentication** — Login, logout, and role-based access
- 🏦 **Account Management** — Create and manage savings/current accounts
- 💸 **Fund Transfers** — Secure atomic transfers between accounts
- 💰 **Deposits & Withdrawals** — Real-time balance updates
- 📋 **Transaction History** — Full log of all financial operations
- 🏠 **Loan Tracking** — View and manage loan applications
- 🔍 **Audit Logs** — Track all system activity
- 🏢 **Branch Management** — Multi-branch support
- 👤 **Customer Profiles** — Linked to Django auth users

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Database | PostgreSQL |
| Frontend | HTML, Tailwind CSS |
| Auth | Django Auth |
| ORM | Django ORM |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bank_system.git
cd bank_system
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database

Edit `banking_system/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'banking_system1',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## 📁 Project Structure
```
bank_system/
├── accounts/        # Account models, views
├── audit/           # Audit log tracking
├── banking_system/  # Project settings, urls
├── branches/        # Branch management
├── customers/       # Customer profiles
├── loans/           # Loan applications
├── static/          # Static files
├── templates/       # HTML templates
├── transactions/    # Transfer, deposit, withdraw
├── users/           # Auth views
└── manage.py
```

---

## 🔑 Default URLs

| URL | Description |
|---|---|
| `/` | Login page |
| `/dashboard/` | Main dashboard |
| `/accounts/` | Account list |
| `/create-account/` | Create new account |
| `/transfer/` | Fund transfer |
| `/deposit/` | Deposit money |
| `/withdraw/` | Withdraw money |
| `/transactions/` | Transaction history |
| `/loans/` | Loan applications |
| `/audit/` | Audit logs |
| `/admin/` | Django admin panel |

---

## 📌 Notes

- Add a `.env` file for sensitive settings before pushing to production
- Never commit `SECRET_KEY` or database passwords to GitHub
- Run `pip freeze > requirements.txt` before pushing

---

## 👨‍💻 Author

Built with ❤️ using Django + PostgreSQL
```

---

**Before pushing to GitHub, make sure to:**

1. Create a `.gitignore` file:
```
venv/
*.pyc
__pycache__/
db.sqlite3
.env
