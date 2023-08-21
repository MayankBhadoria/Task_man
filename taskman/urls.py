from django.contrib import admin
from django.urls import path
from taskman.views import home,login, signup,signout, add, delete, update

urlpatterns = [
    path('',home, name='home'),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
     path('logout/', signout),
     path('tasks/', add, name='add'),
     path('delete/<int:id>', delete),
     path('update/<int:id>', update, name="update",)
]
