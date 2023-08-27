from django.contrib import admin
from VCapp.models import Company, Account, Customer, Feature, Orders
# Register your models here.
admin.site.register(Company)
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Feature)
admin.site.register(Orders)
