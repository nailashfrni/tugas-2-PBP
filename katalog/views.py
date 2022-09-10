from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
katalog = CatalogItem.objects.all()
context = {
    "name": "Naila Shafirni Hidayat",
    "id": 2106638324,
    "katalog":katalog,
}

def show_katalog(request):
    return render(request, "katalog.html", context)