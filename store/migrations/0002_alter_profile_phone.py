# Generated by Django 5.1.2 on 2024-10-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='+* *** *** ****', max_length=18, null=True),
        ),
    ]
