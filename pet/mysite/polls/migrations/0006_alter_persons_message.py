# Generated by Django 5.1.1 on 2024-10-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_persons_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='message',
            field=models.TextField(),
        ),
    ]
