# Generated by Django 2.0.2 on 2018-02-12 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_file_approvers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='approvers',
        ),
    ]