from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from emp_details.models import *
from emp_details.serializers import *
from .serializers import DepartmentSerializer


@api_view(['POST'])
def Dep_add(request):
    data = request.data
    serializer = DepartmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)  # Print serializer errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def man_promote(request, emp_id):
    try:
        # Retrieve the employee profile
        employee = Employee.objects.get(emp_id=emp_id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(
            employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(role='M')  # Set role to 'M' (manager)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def man_demote(request, emp_id):
    try:
        # Retrieve the employee profile
        employee = Employee.objects.get(emp_id=emp_id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Update the role to 'S' (Standard)
    employee.role = 'S'
    employee.save()

    # Serialize the updated employee
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def dept_all(request):
    Profiles = Department.objects.all()
    serializer = DepartmentSerializer(Profiles, many=True)
    return Response(serializer.data)

# delete a dept
@api_view(['DELETE'])
def dept_delete(request, dept_id):
    # Retrieve the employee profile
    dept = Department.objects.get(dept_id=dept_id)

    # Delete the employee profile
    dept.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)