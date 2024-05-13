from django.db import models

# Department object or schema
class Department(models.Model):
    dep_name = models.CharField(max_length=100, unique=True)
    dep_location = models.CharField(max_length=100, unique=True)
    dept_id = models.IntegerField(unique=True)
    man_id = models.ForeignKey('emp_details.Employee', to_field='emp_id', on_delete=models.CASCADE, limit_choices_to={'role': 'M'})

    def __str__(self):
        return self.dep_name
