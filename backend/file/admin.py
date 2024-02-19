from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'file', 'created_at']


admin.site.register(File, FileAdmin)
