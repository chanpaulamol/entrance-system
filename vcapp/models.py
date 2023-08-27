from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    logo = models.ImageField(
        upload_to="images/", height_field=None, width_field=None, max_length=None, help_text="Upload logo")
    tax_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    stamp = models.ImageField(upload_to="images/", height_field=None,
                              width_field=None, max_length=None, help_text="Upload stamp")
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    title = models.CharField(max_length=80)
    username = models.CharField(max_length=50)
    profile = models.ImageField(
        upload_to="images/", height_field=None, width_field=None, max_length=None)

    sex_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=50, choices=sex_choice)

    employee_status = (
        ('is_admin', 'Admin'),
        ('is_employee', 'Employee')
    )

    status = models.CharField(max_length=50, choices=employee_status)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    signature = models.ImageField(
        upload_to="images/", height_field=None, width_field=None, max_length=None)
    password = models.CharField(max_length=20)
    company = models.ForeignKey(
        to=Company, related_name="company", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, default="", unique=True)
    address = models.CharField(max_length=100, null=False, default="")
    phone = models.CharField(max_length=15, default="", unique=True)
    email = models.EmailField(max_length=50, default="", unique=True)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Letter(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(
        to=Account, related_name="salesperson", on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(
        auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.subject


class Orders(models.Model):
    letter = models.ForeignKey(
        to=Letter, related_name="letters", on_delete=models.CASCADE)
    feature = models.ForeignKey(
        to=Feature, related_name="features", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = 'Orders'

        def __str__(self):
            return self.letter.subject


class Invoice(models.Model):
    letter = models.ForeignKey(
        to=Letter, related_name="invoices", on_delete=models.CASCADE, default="")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(
        auto_now=True, auto_now_add=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.Letter.subject


class Receipt(models.Model):
    invoice = models.ForeignKey(
        to=Invoice, related_name="receipts", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
