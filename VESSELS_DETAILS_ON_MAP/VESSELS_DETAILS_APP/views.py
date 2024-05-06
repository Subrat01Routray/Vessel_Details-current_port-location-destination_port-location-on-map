from django.shortcuts import render
from .forms import VesselNumberForm
from .models import RouteDetails

def show_route_details(request):
    if request.method == 'POST':
        form = VesselNumberForm(request.POST)
        if form.is_valid():
            vessel_number = form.cleaned_data['vessel_number']
            route_details = RouteDetails.objects.get(vessel_number=vessel_number)
            
            return render(request, 'route_details.html', {'route_details': route_details})
    else:
        form = VesselNumberForm()
    
    return render(request, 'choose_page.html', {'form': form})
