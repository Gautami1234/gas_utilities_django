from django.urls import path
from . import views

urlpatterns = [
    path('assign/<int:service_request_id>/', views.assign_ticket, name='assign_ticket'),
    # path('assigned/<int:ticket_id>/', views.ticket_assigned, name='ticket_assigned'),
    path('resolve/<int:ticket_id>/', views.resolve_ticket, name='resolve_ticket'),
    path('already_assigned/<int:ticket_id>/', views.ticket_already_assigned, name='ticket_already_assigned'),

]
