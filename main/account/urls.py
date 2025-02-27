from django.urls import path, include
from .views import registerpage, loginpage
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signup/', registerpage, name="signup"),
    path('login/', loginpage, name="login"),
]