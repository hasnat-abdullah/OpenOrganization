# Generated by Django 3.1.7 on 2021-04-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_details', '0008_quote_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
