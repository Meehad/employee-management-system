from django.db import models
from emp_details.models import *

# Department object or schema
class Department(models.Model):
    man_id = models.ForeignKey(Employee, to_field='emp_id',on_delete=models.CASCADE,limit_choices_to={'role': 'M'})
    dep_name=models.CharField(max_length=100,unique=True)
    dep_location=models.CharField(max_length=100,unique=True)
    dept_id=models.IntegerField(unique=True)
    
    def __str__(self) :
        return self.man_id