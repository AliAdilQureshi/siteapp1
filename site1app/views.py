

from django.shortcuts import render
from .models import FileUpload, saf_defect_table
from .main import making_a_doc_function


# Create your views here.
def index(request):

    numbers_from_saf_defect_table = saf_defect_table.objects.all()

    return render(request, "index.html", {


        'numbers_from_saf_defect_table': numbers_from_saf_defect_table,


    })


def making_the_doc(request):

    return making_a_doc_function(request)


