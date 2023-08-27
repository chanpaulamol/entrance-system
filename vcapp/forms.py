from django.forms import ModelForm
from .models import Customer, Letter, Orders, Invoice


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = {'letter', 'due_date'}
