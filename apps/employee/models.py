from django.db import models


class Employee(models.Model):
    post = models.CharField(
        'Должность',
        max_length=500
    )
    post_genitive = models.CharField(
        'Должность в родительном падеже',
        max_length=500
    )
    post_dative = models.CharField(
        'Должность в дательном падеже',
        max_length=500
    )
    full_name = models.CharField(
        'ФИО',
        max_length=1000
    )
    full_name_genitive = models.CharField(
        'ФИО в родительном падеже',
        max_length=1000
    )
    full_name_dative = models.CharField(
        'ФИО в дательном падеже',
        max_length=1000
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '{} ({})'.format(self.full_name, self.post)
