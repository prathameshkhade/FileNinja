# Generated by Django 4.2.11 on 2024-03-31 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File_Ninja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
