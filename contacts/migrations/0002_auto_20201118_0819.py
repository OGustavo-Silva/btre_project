# Generated by Django 3.1.3 on 2020-11-18 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='contatac_date',
            new_name='contact_date',
        ),
    ]
