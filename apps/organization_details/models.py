from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrganizationDetails(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    logo = models.ImageField(upload_to='organization/', blank=True, null=True, db_index=True)
    short_description = models.CharField(max_length=249, blank=True, null=True)
    long_description = models.TextField(max_length=10000, blank=True, null=True)
    address = models.CharField(max_length=249)
    phone = models.CharField(max_length=100)  # so that multiple phone number can be entered
    email = models.CharField(max_length=150)
    website = models.URLField(max_length=50)

    def __str__(self):
        return self.name


class CoverPhoto(BaseModel):
    cover_photo = models.ImageField(upload_to='organization/cover/')
    position = models.SmallIntegerField(null=False, blank=False)
    h1_text = models.CharField(max_length=250, null=True, blank=True)
    h2_text = models.CharField(max_length=250, null=True, blank=True)
    details_text = models.CharField(max_length=250, null=True, blank=True)
    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


class TransectionAccountsCategory(BaseModel):
    """
    bkash, bank, rocket, nagad etc
    """
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class TransectionAccounts(BaseModel):
    bank_name = models.CharField(max_length=60, blank=True, null=True, db_index=True)
    branch_name = models.CharField(max_length=60, blank=True, null=True)
    account_name = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.CharField(max_length=50, db_index=True)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    national_money_transfer_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(TransectionAccountsCategory, on_delete=models.CASCADE)
    current_balance = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category}- {self.account_number}"


class Contact(BaseModel):
    name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(blank=False)
    phn = models.CharField(blank=True,null=True, max_length=20, default=None)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Quote(BaseModel):
    quote_details = models.TextField(max_length=1000)
    reference = models.CharField(max_length=200)
    position = models.PositiveSmallIntegerField(default=0)
    will_show_in_homepage = models.BooleanField(default=True)

    def __str__(self):
        return self.quote_details


class Subscribers(BaseModel):
    email = models.EmailField(max_length=249, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
