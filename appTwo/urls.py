from django.urls import path, re_path
from appTwo import views

urlpatterns = [
    path('',views.users,name='users'),
]