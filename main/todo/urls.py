from django.urls import path, include
from .views import index, edit, delete #, registerpage, loginpage
urlpatterns = [
    path('', index, name="index"),
    path('edit/<int:pk>/', edit, name="edit"),
    path('delete/<int:pk>/', delete, name="delete"),
    path('signup/', include("django.contrib.auth.urls")),
    #path('signup', registerpage, name="signup"),
    #path('login', loginpage, name="login"),
]