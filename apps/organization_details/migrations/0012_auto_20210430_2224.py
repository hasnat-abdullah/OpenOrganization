# Generated by Django 3.1.7 on 2021-04-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_details', '0011_auto_20210429_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(max_length=249, unique=True),
        ),
    ]
