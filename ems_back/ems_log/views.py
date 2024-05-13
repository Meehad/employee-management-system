from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
from django.contrib.auth.hashers import check_password

# registration of a company
@api_view(['POST'])
def company_registration(request):
    data = request.data
    serializer = CompanySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login of a company
@api_view(['POST'])
def company_login(request):
    data = request.data
    try:
        company = Company.objects.get(company_email=data['company_email'])
        if check_password(data['company_pwd'], company.company_pwd):
            serializer = CompanySerializer(company)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
    except Company.DoesNotExist:
        return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
