from django.db import models
from organization_details.models import BaseModel, TransectionAccounts
from organization_activity.models import Projects, FundType
from donation.models import DonationRecord


class CashBalance(BaseModel):
    project = models.OneToOneField(Projects, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.project.name


class DebitCategory(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DebitRecord(BaseModel):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    debited_by = models.CharField(max_length=50, default="Admin")
    debited_to = models.CharField(max_length=100, default="Admin")
    from_fund = models.ForeignKey(FundType, on_delete=models.CASCADE)
    from_account = models.ForeignKey(TransectionAccounts, on_delete=models.CASCADE)
    justification = models.TextField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=249, blank=True, null=True)

    def __str__(self):
        return f"{self.project.name}-{self.amount}-{self.debited_to}"
