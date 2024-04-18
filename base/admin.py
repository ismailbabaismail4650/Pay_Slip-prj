from django.contrib import admin
from . models import Staff, Pay_slip
# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','basic_salary']

class Pay_slipAdmin(admin.ModelAdmin):
    list_display = ['deductions','bonus','monthly_earning']


admin.site.register(Staff, StaffAdmin)
admin.site.register(Pay_slip, Pay_slipAdmin)