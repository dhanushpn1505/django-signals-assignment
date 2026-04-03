# Django Signals Assignment

##  Overview
This project demonstrates the behavior of Django signals with respect to:

1. Synchronous vs Asynchronous execution  
2. Thread execution  
3. Database transaction behavior  

Additionally, a custom Python class (`Rectangle`) is implemented to demonstrate iterable behavior.

---

##  Project Structure

django-signals-assignment/
│
├── config/        # Django project settings  
├── core/          # App containing models, views, signals, rectangle class  
│   ├── signals.py  
│   ├── views.py  
│   ├── models.py  
│   ├── rectangle.py   # Custom Rectangle class  
│
├── manage.py  
├── README.md  

---

##  Q1: Are Django signals synchronous or asynchronous?

**Answer:**  
Django signals are **synchronous by default**.

**Proof:**  
- A delay (`time.sleep(5)`) is introduced inside the signal  
- The HTTP response waits until the signal execution completes  
- This confirms blocking behavior → synchronous execution  

---

##  Q2: Do Django signals run in the same thread?

**Answer:**  
Yes, Django signals run in the **same thread as the caller**.

**Proof:**  
- Printed thread ID inside the view  
- Printed thread ID inside the signal  
- Both IDs match → confirms same thread execution  

---

##  Q3: Do Django signals run in the same database transaction?

**Answer:**  
Yes, Django signals run in the **same database transaction by default**.

**Proof:**  
- An exception is raised inside the signal  
- The entire database operation is rolled back  
- Confirms signals are part of the same transaction  

---

##  Custom Class: Rectangle

Implemented in:  
core/rectangle.py  

### ✔ Features
- Requires `length` and `width` during initialization  
- Supports iteration  
- Outputs values in required format  

###  Example Usage

```python
from core.rectangle import Rectangle

rect = Rectangle(10, 5)

for item in rect:
    print(item)
