from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["ticket_number", "user", "created_at", "admin_response", "status"]  # ✅ Fixed typo
