# Generated by Django 5.1.2 on 2024-10-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_homemessages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemessages',
            name='left_message',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='homemessages',
            name='middle_message',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='homemessages',
            name='right_message',
            field=models.TextField(blank=True, max_length=35, null=True),
        ),
    ]
