# Generated by Django 4.2.2 on 2023-07-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='acctype',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.CharField(max_length=20),
        ),
    ]
