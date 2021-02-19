from django.db import models
from organization_details.models import BaseModel, TransectionAccounts
from organization_activity.models import Projects, FundType


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DonorCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Donor(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    phone = models.CharField(max_length=20,null=True,blank=True,unique=True, db_index=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=249, null=True, blank=True)
    DonorCategory = models.ForeignKey(DonorCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DonationRecord(BaseModel):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, db_index=True)
    donated_in_project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    donation_details = models.CharField(max_length=249, blank=True, null=True)
    donated_to = models.ForeignKey(TransectionAccounts, on_delete=models.CASCADE)
    is_visiable_to_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.donated_in_project}-BDT:{self.amount}-Donated to-{self.donated_to.category}: {self.donated_to.account_number}"
