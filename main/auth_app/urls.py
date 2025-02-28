from django.urls import path,include
from .views import register_view, user_login_view, user_logout_view

urlpatterns=[
    path('signup/', register_view, name="signup"),
    path('login/', user_login_view, name="login"),
    path('todo/', include('todo.urls'))
]