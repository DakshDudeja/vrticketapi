from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "institution_name","date_now","timing","visited"]
admin.site.register(File, FileAdmin)
