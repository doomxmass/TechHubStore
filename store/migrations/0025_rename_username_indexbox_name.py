# Generated by Django 5.1.2 on 2024-10-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_indexbox_sened_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexbox',
            old_name='username',
            new_name='name',
        ),
    ]
