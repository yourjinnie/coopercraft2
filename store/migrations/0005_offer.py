# Generated by Django 5.0.6 on 2024-06-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_pr_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('discount_percentage', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]