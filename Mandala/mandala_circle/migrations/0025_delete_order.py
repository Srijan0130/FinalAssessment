# Generated by Django 3.2.6 on 2021-09-14 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0024_rename_orderplaced_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]