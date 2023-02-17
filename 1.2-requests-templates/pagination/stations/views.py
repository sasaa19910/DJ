from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations_list = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        res = csv.DictReader(csvfile)
        for row in res:
            bus_stations_list.append(row)
    paginator = Paginator(bus_stations_list, 10)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    data = page.object_list

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations':  data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
















# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.conf import settings
# from django.core.paginator import Paginator
# import csv
#
# def index(request):
#     return redirect(reverse('bus_stations'))
#
#
# def bus_stations(request):
#     bus_stations_list = []
#     with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
#         res = csv.DictReader(csvfile)
#         for row in res:
#             bus_stations_list.append(row)
#
#     current_page = int(request.GET.get('page', 1))
#     paginator = Paginator(bus_stations_list, 10)
#     page = paginator.get_page(current_page)
#     new_data = page.object_list
#
#     # получите текущую страницу и передайте ее в контекст
#     # также передайте в контекст список станций на странице
#
#     context = {
#         'bus_stations': bus_stations_list,
#         'page': page,
#     }
#     return render(request, 'stations/index.html', context)
