from django.db import models
from apps.organization_details.models import BaseModel, TransectionAccounts
from apps.organization_activity.models import Projects


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DonorCategory(BaseModel):
    """
    Standard, Silver, Gold, Diamond
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Donor(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='donor_pic/', null=True, blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True,unique=True, db_index=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=249, null=True, blank=True)
    DonorCategory = models.ForeignKey(DonorCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FundType(BaseModel):
    """
    Jatak, fitra etc
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RepeatedDonation(BaseModel):
    WEEKLY = 'W'
    MONTHLY = 'M'
    YEARLY = 'Y'
    FREQUENCY = (
        (WEEKLY,'Weekly'),
        (MONTHLY,'Monthly'),
        (YEARLY,'Yearly'),
    )
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, db_index=True)
    donated_in_project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    fund_type = models.ForeignKey(FundType, on_delete=models.CASCADE)
    donation_details = models.CharField(max_length=249, blank=True, null=True)
    donated_to = models.ForeignKey(TransectionAccounts, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=2, choices=FREQUENCY, default=MONTHLY)
    is_visiable_to_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.donated_in_project}-BDT:{self.amount}-Donated to-{self.donated_to.category}: {self.donated_to.account_number}"


class DonationRecord(BaseModel):
    PENDING = 'P'
    FAILED = 'F'
    SUCCESS = 'S'
    STATUS = (
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
        (SUCCESS, 'Success'),
    )
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, db_index=True)
    donated_in_project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    fund_type = models.ForeignKey(FundType, on_delete=models.CASCADE)
    donation_details = models.CharField(max_length=249, blank=True, null=True)
    donated_to = models.ForeignKey(TransectionAccounts, on_delete=models.CASCADE)
    is_visiable_to_public = models.BooleanField(default=True)
    status = models.CharField(max_length=2, choices=STATUS, default=PENDING)

    def __str__(self):
        return f"{self.donated_in_project}-BDT:{self.amount}-Donated to-{self.donated_to.category}: {self.donated_to.account_number}"
