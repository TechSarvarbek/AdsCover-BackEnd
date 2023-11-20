from django.contrib import admin

from .models import Locations, Keywords, Ad, Company



class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('user',)

class AdAdmin(admin.ModelAdmin):
    search_fields = ('headline',)

class LocationsAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class KeywordsAdmin(admin.ModelAdmin):
    search_fields = ('keyword',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Keywords, KeywordsAdmin)
