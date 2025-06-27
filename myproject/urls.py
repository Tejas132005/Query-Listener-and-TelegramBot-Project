from django.contrib import admin
from django.urls import path, include
from accounts.views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name="main_page"),
    path('accounts/', include('accounts.urls')),  
    path('telegram/', include("telegram_bot.urls")),
    path('complaints/', include('complaints.urls')),  
]