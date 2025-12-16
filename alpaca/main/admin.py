from django.contrib import admin
from .models import Report, Car, Employee, EmployeePosition, Test


admin.site.register(Report)
admin.site.register(Car)
admin.site.register(Employee)
admin.site.register(EmployeePosition)
admin.site.register(Test)
