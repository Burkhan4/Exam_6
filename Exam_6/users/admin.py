from django.contrib import admin
from .models import CustomUser, EmailVerifycationCodes

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'email_verified', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('email_verified', 'is_staff')

@admin.register(EmailVerifycationCodes)
class EmailVerifycationCodesAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'status', 'created_at')
    search_fields = ('email', 'code')
    list_filter = ('status',)
