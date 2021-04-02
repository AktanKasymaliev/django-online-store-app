# Generated by Django 3.1.7 on 2021-03-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_user', '0004_auto_20210331_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]