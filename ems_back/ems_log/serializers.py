from rest_framework import serializers
from .models import Company
from django.contrib.auth.hashers import make_password


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'company_email',
                  'company_contact', 'company_pwd']
    #     extra_kwargs = {
    #         'company_pwd': {'write_only': True}
    #     }

    # def create(self, validated_data):
    #     validated_data['company_pwd'] = make_password(
    #         validated_data['company_pwd'])
    #     return super(CompanySerializer, self).create(validated_data)


class CompanyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_email', 'company_pwd']
