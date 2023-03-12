from django.shortcuts import render
from .models import TableAclass

# Create your views here.
def index(request):
    obj=TableAclass.objects.all()
    context={
        "obj":obj,

    }
    return render(request,"index.html",context)
