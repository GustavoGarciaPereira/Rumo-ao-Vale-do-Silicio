# Generated by Django 2.2.6 on 2020-03-16 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidor', '0003_auto_20200310_2256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estoque',
            new_name='EstoqueDistribuidor',
        ),
    ]