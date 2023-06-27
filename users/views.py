from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.http import request
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Se ha creado la cuenta para {username}! Ahora puedes ingresar.')
            return redirect('login')
        else:
            form = UserRegisterForm()                              #blank form
    form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid:
            u_form.save()
            messages.success(request, f'Información de cuenta actualizada!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)





