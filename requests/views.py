from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from customers.models import Customer

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = Customer.objects.first()

            service_request.save() 
            return redirect('request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/submit_request.html', {'form': form})

def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'requests/track_request.html', {'service_request': service_request})

def request_success(request):
    return render(request, 'requests/request_success.html')