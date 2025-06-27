from rest_framework.views import APIView
from rest_framework import response 
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Ticket
from .serializers import TicketSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

@method_decorator(login_required, name='dispatch')
class DashboardView(APIView):
    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'accounts/dashboard.html', {'tickets':tickets})
    

@method_decorator(login_required, name='dispatch')
class CreateTicketView(APIView):
    def get(self, request):
        return render(request, 'accounts/new_ticket.html')
    
    def post(self, request):
        data = {
            "type" : request.POST.get("type"),
            "title" : request.POST.get("title"),
            "description" : request.POST.get("description"),
            "user" : request.user.id
        }
        serializer = TicketSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return redirect('dashboard')
        return render(request, 'accounts/new_ticket.html', {"errors" : serializer.errors})
    

@method_decorator(login_required, name='dispatch')
class TicketDetailView(APIView):
    def get(self, request, ticket_number):
        ticket = get_object_or_404(Ticket, ticket_number = ticket_number, user=request.user)
        return render(request, 'accounts/ticket_detail.html', {'ticket':ticket})
    
    
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class AdminPanelView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all().order_by('-created_at')
        return render(request, 'complaints/admin_panel.html', {'tickets': tickets})


@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class AdminTicketDetailView(APIView):
    def get(self, request, ticket_number):
        ticket = get_object_or_404(Ticket, ticket_number=ticket_number)
        return render(request, 'complaints/ticket_admin_detail.html', {'ticket': ticket})

    def post(self, request, ticket_number):
        ticket = get_object_or_404(Ticket, ticket_number=ticket_number)
        ticket.admin_response = request.POST.get('admin_response')
        ticket.status = request.POST.get('status')
        ticket.save()
        return redirect('admin_panel')
    

@method_decorator(login_required, name='dispatch')
class CreateTicketView(APIView):
    def get(self, request):
        return render(request, 'accounts/new_ticket.html')
    
    def post(self, request):
        data = {
            "type": request.POST.get("type"),
            "title": request.POST.get("title"),
            "description": request.POST.get("description"),
            "user": request.user.id
        }
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return redirect('dashboard')
        return render(request, 'accounts/new_ticket.html', {"errors": serializer.errors})