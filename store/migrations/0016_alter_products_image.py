# Generated by Django 5.1.2 on 2024-10-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default_files/default_product.png', upload_to='products/%Y%b%d'),
        ),
    ]
