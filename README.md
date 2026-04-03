# Django Signals Assignment

##  Overview
This project demonstrates the behavior of Django signals with respect to:

1. Synchronous vs Asynchronous execution  
2. Thread execution  
3. Database transaction behavior  

All answers are supported with practical code demonstrations inside a Django project.

---

##  Project Structure

- config/ → Django project settings  
- core/ → App containing models, views, and signals  
- manage.py → Entry point  

---

##  Q1: Are Django signals synchronous or asynchronous?

**Answer:**  
Django signals are **synchronous by default**.

**Proof:**  
- A delay (`time.sleep(5)`) is added inside the signal  
- The HTTP response waits until the signal completes  
- This proves signals block execution → synchronous behavior  

---

##  Q2: Do Django signals run in the same thread?

**Answer:**  
Yes, Django signals run in the **same thread as the caller**.

**Proof:**  
- Thread ID printed inside the view  
- Thread ID printed inside the signal  
- Both IDs are identical → same thread execution  

---

##  Q3: Do Django signals run in the same database transaction?

**Answer:**  
Yes, Django signals run in the **same database transaction by default**.

**Proof:**  
- Exception raised inside signal  
- Entire transaction is rolled back  
- Confirms signal is part of same transaction  

---

##  How to Run

```bash
git clone https://github.com/dhanushpn1505/django-signals-assignment.git
cd django-signals-assignment

pip install django

python manage.py migrate
python manage.py runserver
