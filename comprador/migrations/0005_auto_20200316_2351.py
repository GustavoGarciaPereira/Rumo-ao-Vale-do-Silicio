# Generated by Django 2.2.6 on 2020-03-16 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comprador', '0004_auto_20200316_0054'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estoque',
            new_name='EstoqueComprador',
        ),
    ]
