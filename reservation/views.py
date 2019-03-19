from .models import Reservation
from .forms import ReserveTableForm
from django.shortcuts import render


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.method)

        if reserve_form.is_valid():
            reserve_form.save()


    context={'form': reserve_form}
    return render(request, 'Reservation/reservation.html', context)