from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        # print(form)
        return render(request, 'register.html', context)
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account was created for {user.username}')
            return redirect('feed')

        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = { 'form': form }
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})


