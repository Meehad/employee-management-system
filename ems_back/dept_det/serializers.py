from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['dept_id', 'dep_location', 'dep_name', 'man_id']
