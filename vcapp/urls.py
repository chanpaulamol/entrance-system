from django.urls import path
from . import views
urlpatterns = [
    path('accounts/customer/', views.customer, name="customer"),
    path('accounts/customer/add/', views.add_customer, name="add_customer"),
    path('accounts/customer/update/<str:pk>/',
         views.update_customer, name="update_customer"),
    path('accounts/customer/delete/<str:pk>/',
         views.delete_customer, name="delete_customer"),

    path('letter/', views.letter_view, name="letter"),
    path('show', views.show_letter, name="show_letter"),
    path('create', views.create_letter, name="create_letter"),
    path('update/<str:pk>/', views.update_letter, name="update_letter"),
    path('delete/<str:pk>/', views.delete_letter, name="delete_letter"),
    path('letter/download/<str:pk>/', views.GeneratePDF, name="download_letter"),


    path('orders/', views.orders, name="orders"),
    path('orders/delete/<str:pk>/',
         views.delete_order, name="delete_order"),

    path('invoice/', views.invoice, name="invoice"),
    path('invoice/', views.create_invoice, name="add_invoice"),
]
