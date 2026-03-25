
from django.urls import path


from .views import homepage
from .views import about

urlpatterns = [
    path('', homepage),
    path('about/',about),
]