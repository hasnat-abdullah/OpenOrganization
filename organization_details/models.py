from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationDetails(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='organization/', blank=True, null=True)
    short_description = models.CharField(max_length=249, blank=True, null=True)
    long_description = models.TextField(max_length=10000, blank=True, null=True)
    address = models.CharField(max_length=249)
    phone = models.CharField(max_length=100)  # so that multiple phone number can be entered
    email = models.CharField(max_length=150)
    website = models.URLField(max_length=50)

    def __str__(self):
        return self.name


class TransectionAccountsCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class TransectionAccounts(BaseModel):
    bank_name = models.CharField(max_length=60, blank=True, null=True)
    branch_name = models.CharField(max_length=60, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    national_money_transfer_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(TransectionAccountsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}- {self.account_number}"

