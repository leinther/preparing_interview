# Generated by Django 5.1.1 on 2024-10-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_surname_persons_email_persons_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='email',
        ),
    ]
