from django.contrib import admin
from .models import LogEntry
from django.contrib.auth.models import User


admin.site.register(LogEntry)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name','last_name','username','email',)
    list_filter = ('user_id','first_name','last_name','username','email',)
    search_fields = ('user_id','first_name','last_name','username','email',)