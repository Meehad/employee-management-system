from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

# to validate phone no
def validate_contact_number(value):
    if len(str(value)) != 10:
        raise ValidationError('Contact number must be exactly 10 digits.')

# Create your models here.
class Company(models.Model):
    # auto id generate
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255,unique=True)
    company_email = models.EmailField(unique=True)
    company_contact = models.BigIntegerField(
        validators=[validate_contact_number],unique=True)
    company_pwd = models.CharField(max_length=128)

    # def save(self, *args, **kwargs):
    #     # Hash the password before saving
    #     self.company_pwd = make_password(self.company_pwd)
    #     super(Company, self).save(*args, **kwargs)