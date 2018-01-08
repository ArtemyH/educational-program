from django import forms
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from apps.educational_program.models import (
    EducationalProgram, EducationalArea, EducationalCenter, Institute
)


class ProgramForm(forms.ModelForm):
    class Meta:
        model = EducationalProgram
        fields = '__all__'


class ProgramAdmin(admin.ModelAdmin):
    fields = (
        'area', 'center', 'order_on_open_url'
    )
    readonly_fields = ('order_on_open_url', )

    def order_on_open_url(self, instance):
        return mark_safe('<a href={}>{}</a>'.format(instance.order_to_open.url, instance.order_to_open.url))


admin.site.register(EducationalArea)
admin.site.register(EducationalCenter)
admin.site.register(Institute)
admin.site.register(EducationalProgram)
