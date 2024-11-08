# Generated by Django 5.1.2 on 2024-10-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_cart_added_on_remove_cart_products_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=60, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('message', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
