from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    #role and year_0f_exp are read only
    role = serializers.CharField(read_only=True)
    years_of_exp = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'emp_email', 'emp_contact_no', 'date_of_joining', 'role', 'years_of_exp']