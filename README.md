# Django Signals Assignment

## Overview

This project demonstrates the behavior of Django signals with respect to:

1. Synchronous vs Asynchronous execution
2. Thread execution
3. Database transaction behavior



## Q1: Are Django signals synchronous or asynchronous?

**Answer:**
Django signals are synchronous by default.

**Proof:**
A delay (`time.sleep(5)`) inside the signal blocks the response until execution completes.


## Q2: Do Django signals run in the same thread?

**Answer:**
Yes, signals run in the same thread.

**Proof:**
Thread IDs printed in both the view and signal are identical.


## Q3: Do Django signals run in the same transaction?

**Answer:**
Yes, signals run in the same database transaction.

**Proof:**
An exception raised in the signal causes a rollback of the entire transaction.


## How to Run

```bash
git clone <your-repo-link>
cd django-signals-assignment
pip install django
python manage.py migrate
python manage.py runserver
```

---

## Test Endpoint

Visit:

```
http://127.0.0.1:8000/test/
```


## Author

Dhanush P Nambiar
