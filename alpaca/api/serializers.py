from rest_framework import serializers
from ..main.models import EmployeePosition


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePosition
        fields = ('name', 'description')
