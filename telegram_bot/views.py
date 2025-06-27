import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TelegramUser
from django.utils.decorators import method_decorator

class TelegramWebhook(APIView):
    def post(self, request):
        message = request.data.get("message", {})
        text = message.get("text", "")
        from_user = message.get("from", {})

        print("Recieved Message : ", message)

        if text == "/start":
            username = from_user.get("username")
            print("/start from username:", username)

            if username:
                user, created = TelegramUser.objects.get_or_create(username=username)
                print("Saved to DB : ", user, "|New :", created)
                # Optionally, you can send a welcome message here

        return Response({"ok": True})