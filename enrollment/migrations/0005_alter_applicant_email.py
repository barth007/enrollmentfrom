# Generated by Django 5.0.1 on 2024-01-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0004_alter_applicant_govtid_alter_applicant_hearabout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
