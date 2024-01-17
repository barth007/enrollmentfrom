# from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ApplicantForm
from .models import Applicant
import logging
import datetime
from django.utils import timezone


logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return render(request, "index.html")


def enroll(request):
    # load the states from the JSON file
    with open('static/enrollment/json/allStates.json', 'r') as f:
        states = json.load(f)

    sorted_states = sorted(states,  key=lambda x: x['name'])

    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        # logger.log(form)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            if Applicant.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists')
            elif Applicant.objects.filter(phone=phone).exists():
                form.add_error('phone', 'Phone number already exists')
            else:
                applicant = form.save(commit=False)
                applicant.form_submitted_at = timezone.now()
                applicant.save()
                form.save_m2m()
                return redirect('/success/')  # Redirect to a success page
    else:
        form = ApplicantForm(initial={'form_opened_at': timezone.now()})
        # logger.info('Enroll page opened at %s by %s', datetime.now(), request.user.username)

     # pass the states to the template context
    context = {'states':  sorted_states, 'form': form}

    return render(request, "enroll.html", context)


def success(request):
    return render(request, "success.html")


def get_lgas(request, state_name):
    with open('static/enrollment/json/allStates.json', 'r') as f:
        states = json.load(f)

    # Find the state in the list
    state = next((item for item in states if item['name'] == state_name), None)

    # Extract LGAs if the state is found
    lgas = sorted(state['lgas'], key=lambda x: x['name']) if state else []

    # Return LGAs as JSON
    return JsonResponse({'lgas': lgas})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")

def policies(request):
    return render(request, 'policies.html')
