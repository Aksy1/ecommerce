# Generated by Django 4.2.2 on 2023-07-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_account_accountno_alter_account_acctype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acctype',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
