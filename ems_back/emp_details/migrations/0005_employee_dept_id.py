# Generated by Django 4.2.13 on 2024-05-13 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dept_det", "0002_alter_department_dep_name_alter_department_man_id"),
        ("emp_details", "0004_alter_employee_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="dept_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dept_det.department",
                to_field="dept_id",
            ),
        ),
    ]
