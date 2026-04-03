from django.contrib import admin
from django.urls import path
from core.views import test_view   # 👈 ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view),  # 👈 ADD THIS
]