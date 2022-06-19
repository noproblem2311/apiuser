from rest_framework import generics

from .models import profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer
class ProfileDetail(generics.RetrieveDestroyAPIView):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer