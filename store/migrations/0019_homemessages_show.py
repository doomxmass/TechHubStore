# Generated by Django 5.1.2 on 2024-10-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_homemessages_left_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemessages',
            name='show',
            field=models.BooleanField(default=False, null=True),
        ),
    ]