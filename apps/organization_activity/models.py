from django.db import models
from apps.organization_details.models import BaseModel
import os


def project_image_upload_path(instance, filename):
    path = 'projects/image/{project}'.format(project=instance.project.name)
    return os.path.join(path, filename)


class FundType(BaseModel):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Projects(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    logo = models.ImageField(upload_to='projects/', blank=True, null=True)
    short_description = models.CharField(max_length=249, blank=True, null=True)
    long_description = models.TextField(max_length=10000, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=249,blank=True, null=True)
    allowed_fund_category = models.ManyToManyField(FundType,blank=True)
    expected_budget = models.PositiveIntegerField(null=True,blank=True, default=0)
    collected_money = models.PositiveIntegerField(null=True,blank=True, default=0)
    is_active = models.BooleanField(default=True)
    still_raising_fund = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProjectsGallary(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=project_image_upload_path, blank=True, null=True)
    short_description = models.CharField(max_length=249, blank=True, null=True)
    long_description = models.TextField(max_length=10000, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project.name
