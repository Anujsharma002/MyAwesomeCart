# Generated by Django 5.1.1 on 2024-09-21 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_address1_order_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='message',
        ),
    ]
