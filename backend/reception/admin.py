from django.contrib import admin
# Register your models here.
from django_jalali.admin.filters import JDateFieldListFilter
from .models import Accommodation , Person
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_date', JDateFieldListFilter),
        ('arrival_date', JDateFieldListFilter),
        ('departure_date', JDateFieldListFilter)
    )
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["first_name","last_name","national_code","first_time_pilgrim","gender"]
