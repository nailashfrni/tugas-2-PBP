from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    katalog = CatalogItem.objects.all()
    context = {
        "name": "Naila Shafirni Hidayat",
        "id": 2106638324,
        "katalog":katalog,
    }
    return render(request, "katalog.html", context)