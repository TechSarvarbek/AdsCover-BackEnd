from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    search_fields  = ('email', 'telegram_name',)


admin.site.register(Users, UsersAdmin)