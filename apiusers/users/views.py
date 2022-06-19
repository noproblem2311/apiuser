from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import profile
def profile_list(request):
    MAX_OBJECTS = 20
    profiles = profile.objects.all()[:MAX_OBJECTS]
    data = {"results": list(profiles.values("name", "email", "phone", "time_created"))}


    return JsonResponse(data)
