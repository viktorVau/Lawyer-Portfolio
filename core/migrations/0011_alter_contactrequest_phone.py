# Generated by Django 5.1.7 on 2025-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_client_email_contactrequest_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
