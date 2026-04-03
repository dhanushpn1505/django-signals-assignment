from django.http import HttpResponse
from .models import TestModel
import threading

def test_view(request):
    print("View Thread:", threading.current_thread().name)

    TestModel.objects.create(name="Test")

    return HttpResponse("Check terminal")