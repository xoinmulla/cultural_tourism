from .models import Destination, TourismEvent, Package,Event
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database

            # Send an email notification (configure EMAIL settings in settings.py)
            send_mail(
                subject=form.cleaned_data['subject'],
                message=f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@example.com'],  # Change to your email
            )

            return redirect('contact_success')  # Redirect after submission

    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

from django.shortcuts import render, get_object_or_404
from .models import Destination

def destination_detail(request, destination_id):  
    destination = Destination.objects.get(id=destination_id)  


def festivals(request):
    return render(request, 'festivals.html')

def destination_detail(request, id):  # Ensure the parameter name matches
    destination = Destination.objects.get(id=id)  # Use id here
    events = Event.objects.filter(destination=destination)
    packages = Package.objects.filter(destination=destination)

    return render(request, 'destination_detail.html', {
        'destination': destination,
        'events': events,
        'packages': packages
    })

