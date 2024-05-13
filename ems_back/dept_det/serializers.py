from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = ['dept_id','dept_location','dept_name','man_id']