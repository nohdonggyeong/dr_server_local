# Generated by Django 3.1.7 on 2021-03-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_equipments', '0003_auto_20210308_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usage',
            name='usage_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]