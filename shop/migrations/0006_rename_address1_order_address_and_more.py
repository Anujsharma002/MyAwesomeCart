# Generated by Django 5.1.1 on 2024-09-21 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address2',
            new_name='text_json',
        ),
    ]
