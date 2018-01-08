import os

from django.conf import settings


def get_docx_template_path(filename):
    return os.path.join(settings.DOCX_TEMPLATE_DIR, filename)
