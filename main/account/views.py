from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.
#def registerpage(request):
#    form=CreateUserForm()
#    if request.method=='POST':
#        form=CreateUserForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('login')
#    context={'form':form}
#    return render(request, 'account/signup.html', context)
#
#def loginpage(request):
#
#    context={}
#    return render(request, 'account/login.html', context)
