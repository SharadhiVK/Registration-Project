from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Registration
from .forms import RegistrationForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Registration System")

def create_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registration created successfully'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def get_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    data = {
        'id': registration.id,
        'name': registration.name,
        'email': registration.email,
        'date_of_birth': registration.date_of_birth.strftime('%Y-%m-%d'),
        'created_at': registration.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': registration.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    }
    return JsonResponse(data)

def update_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    if request.method == 'PUT':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registration updated successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def delete_registration(request, id):
    registration = get_object_or_404(Registration, pk=id)
    registration.delete()
    return JsonResponse({'message': 'Registration deleted successfully'})

