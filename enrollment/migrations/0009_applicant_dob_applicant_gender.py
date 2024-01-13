# Generated by Django 5.0.1 on 2024-01-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0008_remove_applicant_aim_remove_applicant_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='dob',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=10, null=True),
        ),
    ]
