print("SIGNALS FILE LOADED")  # 👈 DEBUG LINE

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import threading
from django.db import connection

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, created, **kwargs):
    print("\n--- SIGNAL TRIGGERED ---")
    print("Signal executed (SYNCHRONOUS)")
    print("Signal Thread:", threading.current_thread().name)
    print("In transaction:", connection.in_atomic_block)