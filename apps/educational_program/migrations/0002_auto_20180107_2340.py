# Generated by Django 2.0.1 on 2018-01-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalprogram',
            name='order_to_open',
            field=models.FilePathField(blank=True, null=True, verbose_name='Приказ об открытии'),
        ),
    ]
