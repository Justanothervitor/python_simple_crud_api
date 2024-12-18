# Generated by Django 5.1.2 on 2024-12-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('product_price', models.DecimalField(decimal_places=1, max_digits=7)),
                ('product_description', models.CharField(max_length=255)),
                ('product_vendor', models.CharField(max_length=16)),
            ],
        ),
    ]
