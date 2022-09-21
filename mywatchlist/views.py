from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchList

# Create your views here.
def show_watchlist(request):
    watchlist = MyWatchList.objects.all()
    context = {
        "name": "Naila Shafirni Hidayat",
        "id": 2106638324,
        "watchlist": watchlist,
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")