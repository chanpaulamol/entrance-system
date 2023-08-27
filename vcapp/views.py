from EntranceServiceApp.utils import render_to_pdf
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.urls import reverse
from .forms import CustomerForm, LetterForm, OrderForm, InvoiceForm
from VCapp.models import Customer, Letter, Orders, Feature, Invoice, Account, Company


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def customer(request):
    template = loader.get_template('accounts/customers/customer.html')
    customer = Customer.objects.all()
    total_customers = customer.count()
    context = {
        'customers': customer,
        'total_customers': total_customers,
    }
    return HttpResponse(template.render(context, request))


def add_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer'))

    template = loader.get_template('accounts/customers/customer_form.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def update_customer(request, pk):
    template = loader.get_template('accounts/customers/customer_form.html')
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer'))

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def delete_customer(request, pk):
    template = loader.get_template("accounts/customers/delete.html")
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return HttpResponseRedirect(reverse('customer'))

    context = {
        'customers': customer,
    }
    return HttpResponse(template.render(context, request))

# Letter Handling


def letter_view(request):
    template = loader.get_template("letter/letter.html")
    letters = Letter.objects.all()
    context = {
        'letters': letters,
    }
    return HttpResponse(template.render(context, request))


def show_letter(request):
    template = loader.get_template("letter/show.html")
    letter = Letter.objects.all()
    context = {
        'letter': letter,
    }
    return HttpResponse(template.render(context, request))


def create_letter(request):
    template = loader.get_template("letter/letter_form.html")
    letter_form = LetterForm()
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('letter'))
    context = {
        'form': letter_form,
    }
    return HttpResponse(template.render(context, request))


def update_letter(request, pk):
    template = loader.get_template("letter/letter_form.html")
    letter = Letter.objects.get(id=pk)
    form = LetterForm(instance=letter)
    if request.method == 'POST':
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('letter'))

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def delete_letter(request, pk):
    template = loader.get_template("letter/delete.html")
    letter = Letter.objects.get(id=pk)
    if request.method == "POST":
        letter.delete()
        return HttpResponseRedirect(reverse('letter'))

    context = {
        'letter': letter,
    }
    return HttpResponse(template.render(context, request))


# Orders handling

def orders(request):
    template = loader.get_template("orders/orders.html")
    orders = Orders.objects.all()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orders'))
    context = {
        'form': form,
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


def delete_order(request, pk):
    template = loader.get_template("orders/delete.html")
    order = Orders.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return HttpResponseRedirect(reverse('orders'))

    context = {
        'order': order,
    }
    return HttpResponse(template.render(context, request))

# Invoice


def invoice(request):
    template = loader.get_template("invoices/invoice.html")
    form = InvoiceForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def create_invoice(request):
    template = loader.get_template("invoices/invoice.html")
    letter_id = request.POST['letter_id']
    due_date = request.POST['due_date']

    invoice = Invoice()
    orders.save()
    form = InvoiceForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def dashboard(request):
    template = loader.get_template("dashboard/dashboard.html")
    customer = Customer.objects.all()
    number_customers = customer.count()
    letter = Letter.objects.all()
    number_letters = letter.count()

    features = Feature.objects.all()

    orders = Orders.objects.select_related()
    number_orders = orders.count()

    context = {
        'number_customers': number_customers,
        'number_letters': number_letters,
        'number_orders': number_orders,
        'features': features,
    }
    return HttpResponse(template.render(context, request))

# Automaticly downloads to PDF file


def GeneratePDF(request, pk, *args, **kwargs):
    letter = Letter.objects.filter(id=pk)
    feature = Feature.objects.raw("SELECT * FROM mainapp_feature")
    accounts = Account.objects.all()
    company = Company.objects.all()
    customer = Customer.objects.all()
    salesperson_id = Letter.objects.raw(
        "SELECT DISTINCT salesperson_id FROM mainapp_letter")
    orders = Orders.objects.raw(
        "SELECT DISTINCT o.letter_id, l.subject, o.id FROM mainapp_order AS o INNER JOIN mainapp_letter AS l on o.letter_id=l.id")
    context = {
        'letters': letter,
        'features': feature,
        'accounts': accounts,
        'customers': customer,
        'company': company,
        'salesperson_id': salesperson_id,
        'orders': orders,
    }
    pdf = render_to_pdf('letter/show.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
