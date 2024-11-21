from django.contrib import admin
from .models import CustomUser, Trip

# Foydalanuvchi modelini ro'yxatdan o'tkazish
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'is_premium')
    search_fields = ('username', 'email', 'full_name')

# Sayohat modelini ro'yxatdan o'tkazish
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'start_date', 'end_date')
    search_fields = ('name', 'user__username')
