# Generated by Django 2.0.1 on 2018-01-06 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование области')),
            ],
            options={
                'verbose_name': 'Область образовательной программы',
                'verbose_name_plural': 'Области образовательных программ',
            },
        ),
        migrations.CreateModel(
            name='EducationalCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование центра')),
            ],
            options={
                'verbose_name': 'Научно-образовательный центр',
                'verbose_name_plural': 'Научно-образовательные центры',
            },
        ),
        migrations.CreateModel(
            name='EducationalProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование образовательной программы')),
                ('volume', models.FloatField(verbose_name='Объем в часах')),
                ('start_date', models.DateField(verbose_name='Дата начала курса')),
                ('purpose', models.CharField(max_length=1000, verbose_name='Цель образовательной программы')),
                ('schedule', models.FloatField(help_text='Не более указанного числа часов в день', verbose_name='Режим обучения')),
                ('form', models.IntegerField(choices=[(0, 'Очная'), (1, 'Заочная'), (2, 'Дистанционная')], default=0, verbose_name='Форма обучения')),
                ('order_to_open', models.FileField(blank=True, null=True, upload_to='', verbose_name='Приказ об открытии')),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='programs_in_account', to='employee.Employee', verbose_name='Бухгалтер')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='educational_program.EducationalArea', verbose_name='Область образовательной программы')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='educational_program.EducationalCenter', verbose_name='Научно-образовательный центр')),
                ('checker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='programs_in_check', to='employee.Employee', verbose_name='Контролирующий исполнение')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='programs_in_head', to='employee.Employee', verbose_name='Руководитель программы')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование института')),
            ],
            options={
                'verbose_name': 'Институт',
                'verbose_name_plural': 'Институты',
            },
        ),
        migrations.AddField(
            model_name='educationalprogram',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='educational_program.Institute', verbose_name='Институт'),
        ),
    ]
