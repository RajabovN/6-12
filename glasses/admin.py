from django.contrib import admin
from .models import Eyewear


class EyewearAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')
    list_filter = ('price', 'quantity')
    ordering = ('price', )

admin.site.register(Eyewear, EyewearAdmin)
# Register your models here.
