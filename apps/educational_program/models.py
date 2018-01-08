from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
from docxtpl import DocxTemplate

from apps.employee.models import Employee
from core.utils import get_docx_template_path


class EducationalArea(models.Model):
    name = models.CharField(
        'Наименование области',
        max_length=1000
    )

    class Meta:
        verbose_name = 'Область образовательной программы'
        verbose_name_plural = 'Области образовательных программ'

    def __str__(self):
        return self.name


class EducationalCenter(models.Model):
    name = models.CharField(
        'Наименование центра',
        max_length=1000
    )

    class Meta:
        verbose_name = 'Научно-образовательный центр'
        verbose_name_plural = 'Научно-образовательные центры'

    def __str__(self):
        return self.name


class Institute(models.Model):
    name = models.CharField(
        'Наименование института',
        max_length=1000
    )

    class Meta:
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'

    def __str__(self):
        return self.name


class EducationalProgram(models.Model):
    area = models.ForeignKey(
        to=EducationalArea,
        on_delete=models.PROTECT,
        verbose_name='Область образовательной программы'
    )
    center = models.ForeignKey(
        to=EducationalCenter,
        on_delete=models.PROTECT,
        verbose_name='Научно-образовательный центр'
    )
    institute = models.ForeignKey(
        to=Institute,
        on_delete=models.PROTECT,
        verbose_name='Институт'
    )
    name = models.CharField(
        'Наименование образовательной программы',
        max_length=1000
    )
    volume = models.FloatField(
        'Объем в часах'
    )
    start_date = models.DateField(
        'Дата начала курса'
    )
    head = models.ForeignKey(
        to=Employee,
        on_delete=models.PROTECT,
        verbose_name='Руководитель программы',
        related_name='programs_in_head'
    )
    checker = models.ForeignKey(
        to=Employee,
        on_delete=models.PROTECT,
        verbose_name='Контролирующий исполнение',
        related_name='programs_in_check'
    )
    accountant = models.ForeignKey(
        to=Employee,
        on_delete=models.PROTECT,
        verbose_name='Бухгалтер',
        related_name='programs_in_account'
    )
    purpose = models.CharField(
        'Цель образовательной программы',
        max_length=1000
    )
    schedule = models.FloatField(
        'Режим обучения',
        help_text='Не более указанного числа часов в день'
    )

    class EducationalForm:
        INTERNAL = 0
        CORRESPONDENCE = 1
        REMOTE = 2

        CHOICES = (
            (INTERNAL, 'Очная'),
            (CORRESPONDENCE, 'Заочная'),
            (REMOTE, 'Дистанционная'),
        )

    form = models.IntegerField(
        'Форма обучения',
        choices=EducationalForm.CHOICES,
        default=EducationalForm.INTERNAL
    )
    order_to_open = models.FilePathField(
        'Приказ об открытии',
        path=settings.MEDIA_ROOT,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        doc = DocxTemplate(get_docx_template_path("open_course.docx"))
        context = {'educational_area': self.area}
        doc.render(context)
        filename = "open_course_{}.docx".format(self.id)
        path = "docs/{}".format(filename)
        doc.save(path)
        self.order_to_open = path
