# Generated by Django 4.1.2 on 2022-12-15 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VCapp', '0004_invoice_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='Letter',
            new_name='letter',
        ),
    ]
