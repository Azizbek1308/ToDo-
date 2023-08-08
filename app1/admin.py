from django.contrib import admin
from .models import Smartphone

class SmartphponeAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'cost', 'status')
    def has_add_permission(self, request):
        return False

# Register your models here.
admin.site.register(Smartphone, SmartphponeAdmin)
