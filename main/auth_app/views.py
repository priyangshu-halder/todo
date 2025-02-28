from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('login')
    else:
        initial_data={'username':'', 'password1':'', 'password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request, 'auth_app/register.html', {'form':form})
def user_login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return render(request, 'todo/index.html')
    else:
        initial_data={'username':'', 'password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request, 'auth_app/login.html')
def user_logout_view(request):
    logout(request)
    return redirect('login')