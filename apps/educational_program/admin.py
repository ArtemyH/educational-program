from django.contrib import admin

from apps.educational_program.models import (
    EducationalProgram, EducationalArea, EducationalCenter, Institute
)

admin.site.register(EducationalArea)
admin.site.register(EducationalCenter)
admin.site.register(Institute)
admin.site.register(EducationalProgram)
