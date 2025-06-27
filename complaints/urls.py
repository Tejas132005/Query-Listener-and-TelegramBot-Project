from django.urls import path 
from .views import DashboardView, CreateTicketView, TicketDetailView, AdminPanelView, AdminTicketDetailView

urlpatterns = [  
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('new-ticket/', CreateTicketView.as_view(), name="new_ticket"),
    path('ticket/<str:ticket_number>/', TicketDetailView.as_view(), name='ticket_detail'),

    # Admin panel
    path('admin-panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin-panel/<str:ticket_number>/', AdminTicketDetailView.as_view(), name='admin_ticket_detail'),
]
