from django.contrib import admin
from .models import FileUpload, saf_defect_table, Report_File_Upload_Table

# Register your models here.
admin.site.register(FileUpload)
admin.site.register(saf_defect_table)
admin.site.register(Report_File_Upload_Table)
