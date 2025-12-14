from django.contrib import admin
from .models import Report, Car, Employee, EmployeePosition


admin.site.register(Report)
admin.site.register(Car)
admin.site.register(Employee)
admin.site.register(EmployeePosition)
