from django.contrib import admin

from .models import Payments


class PaymentsAdmin(admin.ModelAdmin):
    search_fields  = ('user',)


admin.site.register(Payments, PaymentsAdmin)