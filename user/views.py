from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import UserForm
from user.models import User


def new_user_oauth(request):
    if request.user.is_anonymous:
        return redirect('login-user')
    form = UserForm(data=request.POST or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all_users')
    else:
        return render(request, 'new_user_oauth.html', {'form': form})


def login(request):
    return render(request, 'login.html', {})


def all_users(request):
    if request.user.is_anonymous:
        return redirect('login-user')
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})


def root_redirect(request):
    return redirect('all_users')
