# Generated by Django 4.2.13 on 2024-05-13 19:03

from django.db import migrations, models
import ems_log.models


class Migration(migrations.Migration):
    dependencies = [
        ("ems_log", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="company_contact",
            field=models.BigIntegerField(
                unique=True, validators=[ems_log.models.validate_contact_number]
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
