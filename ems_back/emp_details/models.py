from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.

# to validate phone no


def validate_contact_number(value):
    if len(str(value)) != 10:
        raise ValidationError('Contact number must be exactly 10 digits.')

# Employee object or schema


class Employee(models.Model):
    EMPLOYEE_ROLE_CHOICES = [
        ('E', 'Eligible for Promotion'),
        ('M', 'Manager'),
        ('S', 'Standard'),
    ]
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_contact_no = models.BigIntegerField(
        validators=[validate_contact_number])
    date_of_joining = models.DateField()
    role = models.CharField(
        max_length=1, choices=EMPLOYEE_ROLE_CHOICES)

    # automatically fills exp with date_of_joining
    @property
    def years_of_exp(self):
        today = date.today()
        return today.year - self.date_of_joining.year - ((today.month, today.day) < (self.date_of_joining.month, self.date_of_joining.day))
