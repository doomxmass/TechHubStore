# Generated by Django 5.1.2 on 2024-10-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_products_date_alter_tags_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='C:\\Users\\doomx\\Desktop\\techhubStore\\main\\default_files\\default_product.png', upload_to='products/%Y%b%d'),
        ),
    ]
