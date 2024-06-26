# Generated by Django 4.2.13 on 2024-05-13 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emp_id", models.IntegerField()),
                ("emp_name", models.CharField(max_length=100)),
                ("emp_email", models.EmailField(max_length=254)),
                (
                    "emp_contact_no",
                    models.BigIntegerField(
                        validators=[
                            django.core.validators.MinLengthValidator(10),
                            django.core.validators.MaxLengthValidator(10),
                        ]
                    ),
                ),
                ("date_of_joining", models.DateField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("E", "Eligible for Promotion"),
                            ("M", "Manager"),
                            ("S", "Standard"),
                        ],
                        default="S",
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]
