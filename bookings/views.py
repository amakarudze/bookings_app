from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    data = {
        'new_booking_name': request.POST.get('booking_name', ''),
        'new_start_date': request.POST.get('start_date',''),
        'new_end_date': request.POST.get('end_date')
        }
    return render(request, 'bookings/index.html', {'data': data})
