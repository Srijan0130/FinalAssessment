# Generated by Django 3.2.6 on 2021-09-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0004_alter_commission_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommissionReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Req_name', models.CharField(max_length=100)),
            ],
        ),
    ]