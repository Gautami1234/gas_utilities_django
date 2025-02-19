# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
            #  return render(request, 'customers/registration_success.html')
    else:
        form = CustomerForm()
    return render(request, 'customers/register_customer.html', {'form': form})

def registration_success(request):
    return render(request, 'customers/registration_success.html')