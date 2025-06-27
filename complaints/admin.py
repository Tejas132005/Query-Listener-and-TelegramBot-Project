from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'title', 'type', 'status', 'user', 'created_at')
    list_filter = ('status', 'type')
    search_fields = ('ticket_number', 'title', 'user__username')
