# Generated by Django 5.1.1 on 2024-09-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(default='', max_length=12)),
                ('email', models.IntegerField(default=70)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
