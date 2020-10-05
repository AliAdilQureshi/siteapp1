from django.db import models

class FileUpload(models.Model):
    attribution_file_upload = models.FileField()

    def __str__(self):
        return self.attribution_file_upload.name[:50]
#above line showing the first 50 charicters of a fileupload files title in django admin

class saf_defect_table(models.Model):
     saf_number_in_table = models.FloatField()
     defect_number_in_table = models.FloatField()




#generated output file upload so users can pull from the file from this db table and view the output report
class Report_File_Upload_Table(models.Model):
    generated_report_file_upload = models.FileField()

    def __str__(self):
        return self.generated_report_file_upload.name[:50]