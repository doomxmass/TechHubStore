# Generated by Django 5.1.2 on 2024-10-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_homemessages_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='added_on',
            field=models.DateField(auto_now=True),
        ),
    ]
