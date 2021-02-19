# Generated by Django 3.1.7 on 2021-02-19 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization_activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='projects',
            name='allowed_fund',
        ),
        migrations.AddField(
            model_name='projects',
            name='still_raising_fund',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='ProjectsGallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/image')),
                ('short_description', models.CharField(blank=True, max_length=249, null=True)),
                ('long_description', models.TextField(blank=True, max_length=10000, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization_activity.projects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='allowed_fund_category',
            field=models.ManyToManyField(blank=True, to='organization_activity.FundType'),
        ),
    ]
