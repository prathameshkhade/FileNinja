# Generated by Django 4.2.11 on 2024-04-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('File_Ninja', '0004_subscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='premium_pack',
            field=models.IntegerField(default=49),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='value_pack',
            field=models.IntegerField(default=29),
        ),
    ]
