# cafe/views.py
from django.shortcuts import render
from .models import Category

# Create your views here.
def rich_cafe(request):
    categorys = Category.objects.all()
    context ={
        "lions" : categorys
    }
    return render(request,"cafe/rich_cafe.html", context)

