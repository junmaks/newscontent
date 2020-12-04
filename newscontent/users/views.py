from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UserAdminCreationForm, UserAdminChangeForm, UserLoginForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterForm()
    return render(request=request, template_name='users/register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request=request, template_name='users/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')