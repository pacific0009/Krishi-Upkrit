# Generated by Django 2.1.7 on 2019-08-21 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krishi_parijan', '0002_mpnroutingtable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MPN',
            new_name='MPNTable',
        ),
    ]