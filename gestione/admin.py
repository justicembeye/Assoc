from django.contrib import admin
from .models import Department, Member, District, City

# Register your models here.
admin.site.register(Department)
admin.site.register(Member)
admin.site.register(District)
admin.site.register(City)