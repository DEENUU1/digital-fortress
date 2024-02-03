from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_active', 'is_staff', 'is_superuser')


admin.site.register(UserAccount, UserAccountAdmin)
