from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

# addition of emplyee


@api_view(['POST'])
def emp_add(request):
    data = request.data
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        employee = serializer.save()

        # Calculate the role based on the years of experience of the saved employee
        role = calculate_role(employee)

        # Update the role field of the saved employee
        employee.role = role
        employee.save()

        # Re-serialize the updated employee
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)  # Print serializer errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# calculate role of employee according to years_of_exp
def calculate_role(instance):
    if instance.years_of_exp >= 5:
        return 'E'
    else:
        return 'S'
# show all employees


@api_view(['GET'])
def emp_all(request):
    profiles = Employee.objects.all()
    serializer = EmployeeSerializer(profiles, many=True)
    return Response(serializer.data)

# delete a employee


@api_view(['DELETE'])
def emp_delete(request, emp_id):
    # Retrieve the employee profile
    employee = Employee.objects.get(emp_id=emp_id)

    # Delete the employee profile
    employee.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
