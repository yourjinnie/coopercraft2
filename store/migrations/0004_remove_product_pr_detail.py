# Generated by Django 5.0.6 on 2024-06-26 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pr_detail',
        ),
    ]