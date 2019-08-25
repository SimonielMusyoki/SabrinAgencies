from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

PROJECT_STATUS = (
        ('Completed', 'Complete'),
        ('Ongoing', 'Ongoing'),
    )

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Title the post will bear")
    content = models.TextField(help_text="The actual Blog Post")
    url = models.URLField(help_text="Any outside link", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

class Projects(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the project")
    idea = models.CharField(max_length=100, blank=True, null=True, help_text="The idea behind the project")
    technologies = models.CharField(max_length=100, blank=True, null=True, help_text="The technologies which have made the project")
    date_started = models.DateTimeField(default=timezone.now)
    git_link = models.URLField(blank=True, null=True, help_text="GitHub link to the project")
    project_link = models.URLField(blank=True, null=True, help_text="The website of the project online")
    status = models.CharField(max_length=100, choices=PROJECT_STATUS, default='completed', help_text="Status of the project")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})

class Messages(models.Model):
    name = models.CharField(max_length=100, help_text="Please enter your full name")
    email = models.EmailField(help_text="Please enter your email")
    message = models.TextField(help_text="Please enter your message")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        message = 'message submitted successfully. Wait for response in your email'
        return reverse('blog-home')

class Properties(models.Model):
    PropertyName = models.CharField(max_length=255, help_text="The Name of the property")
    Address = models.CharField(max_length=255, help_text="The address of the above property")
    City = models.CharField(max_length=255, help_text="The city where the property is located")
    County = models.CharField(max_length=100, help_text="The county of the city above")
    Picture1 = models.ImageField(help_text="Attach first image of your property")
    Picture2 = models.ImageField(help_text="Attach second image of your property", blank=True, null=True)
    Picture3 = models.ImageField(help_text="Attach third image of your property", blank=True, null=True)
    Picture4 = models.ImageField(help_text="Attach fourth image of your property", blank=True, null=True)

    def __str__(self):
        return self.PropertyName

    def get_absolute_url(self):
        return reverse('home')

class Units(models.Model):
    unit_status = (
        ('vacant','VACANT'),
        ('occupied','OCCUPIED'),
        ('closed','CLOSED'),
    )
    UnitNumber = models.CharField(max_length=255, unique=True)
    PropertyID = models.ForeignKey(Properties,help_text="The property number where this unit exists", on_delete=models.CASCADE)
    Floor = models.IntegerField(help_text="The floor of the unit")
    Bedrooms=models.IntegerField(help_text="Number of bedrooms in the units")
    Bathrooms = models.IntegerField(help_text="Number of bathrooms the unit has")
    Status = models.CharField(max_length=10, choices=unit_status)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('units')

    def __str__(self,*args, **kwargs):
        return self.UnitNumber

class Tenant(models.Model):
    UnitID=models.ForeignKey(Units, help_text="The unit this tenant occupies", on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=100, help_text="First name")
    LastName=models.CharField(max_length=255,help_text="Last name")

    def __str__(self):
        return self.FirstName


class Lease(models.Model):
    active_choices=(
        ('Yes',"YES"),
        ('No',"NO")
    )
    PropertyID = models.ForeignKey(Properties, on_delete=models.CASCADE,help_text="Property nae")
    UnitID = models.ForeignKey(Units, on_delete=models.CASCADE,help_text="The unit to let ")
    TenantID = models.ForeignKey(Tenant, on_delete=models.CASCADE,help_text="Start Date")
    StartDate = models.DateTimeField(auto_now_add=True, help_text="Contract Deadline")
    EndDate = models.DateTimeField(help_text="End date", blank=True, null=True)
    Active=models.CharField(max_length=3, choices=active_choices)
    Rent = models.DecimalField(help_text="The rent to this unit", decimal_places=2,max_digits=8)

class Payment(models.Model):
    UnitID = models.ForeignKey(Units, on_delete=models.CASCADE)
    LeaseID = models.ForeignKey(Lease, on_delete=models.CASCADE)
    PaymentAmount = models.DecimalField(decimal_places=2,max_digits=9, help_text="Amount of Money Paid")
    PaymentDate = models.DateTimeField(auto_now_add=True)


class Vendor(models.Model):
    VendorName = models.CharField(max_length=255, help_text="Enter the vendo name")
    Phone = models.CharField(max_length=255, help_text="Phone number of the vendor")
    ContactPerson = models.CharField(max_length=255)
    Email = models.EmailField(max_length=25, help_text="Email address")

    def __str__(self):
        return self.VendorName


class Expense(models.Model):
    expenseTypes = (
        ('plumbing',"Plumping"),
        ('electrical',"Electrical"),
        ('repair and mantinence', "Repair and Maintenance")
    )
    PropertyID = models.ForeignKey(Properties, on_delete=models.CASCADE)
    UnitID = models.ForeignKey(Units, on_delete=models.CASCADE)
    VendorID = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Type = models.CharField(max_length=255, choices=expenseTypes)
    Cost = models.DecimalField(decimal_places=2, max_digits=9)
    Date = models.DateTimeField(auto_now_add=True)
    Reciept = models.FileField(upload_to='media/Receipts/', help_text="Picture of the receipt")
    isPaid = models.BooleanField(default=True)

