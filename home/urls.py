
from django.urls import path


from .views import homepage
from .views import getpost,createpost,editpost,deletepost

urlpatterns = [
    path('', homepage,name='home'),
    path('post/<int:id>/',getpost,name='post'),
    path('create/',createpost,name='create'),
    path('edit/<int:id>/',editpost,name='edit'),
    path('delete/<int:id>/',deletepost,name='delete'),

]