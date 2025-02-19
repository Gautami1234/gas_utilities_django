from django.shortcuts import render, redirect, get_object_or_404
from .models import SupportTicket , ServiceRequest
from django.db import IntegrityError
from django.utils import timezone
from django.urls import reverse




def assign_ticket(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, id=service_request_id)
    
    # Create a new SupportTicket only if one doesn't already exist
    ticket, created = SupportTicket.objects.get_or_create(service_request=service_request)

    # Redirect only if needed
    if created:
        return redirect('assign_ticket', service_request_id=ticket.service_request.id)

    return render(request, 'support/ticket_assigned.html', {'ticket': ticket})
    

def resolve_ticket(request, ticket_id):
    ticket = get_object_or_404(SupportTicket, id=ticket_id)

    if request.method == "POST" and ticket.status != "Resolved":
        resolution = request.POST.get("resolution")
        
        ticket.service_request
        ticket.assigned_at
        ticket.status = "Resolved"
        ticket.resolution_notes = resolution

        ticket.save()

        return redirect('resolve_ticket', ticket_id=ticket.id)  # Refresh page

    return render(request, 'support/resolve_ticket.html', {'ticket': ticket})

# def ticket_assigned(request,ticket_id):
    return redirect(reverse('ticket_assigned', kwargs={'ticket_id': ticket_id}))


def ticket_already_assigned(request,ticket_id):
    return render(request, 'support/ticket_already_assigned.html',{'ticket_id': ticket_id})