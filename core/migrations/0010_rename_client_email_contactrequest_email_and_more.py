# Generated by Django 5.1.7 on 2025-03-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_experience_is_current'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactrequest',
            old_name='client_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactrequest',
            old_name='client_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='contactrequest',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
