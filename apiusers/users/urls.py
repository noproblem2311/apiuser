from django.urls import path
from .views import  profile_list
urlpatterns = [
    path("profile/", profile_list, name="profile_list")
]

from django.urls import path
from .apiviews import ProfileList, ProfileDetail
urlpatterns = [
    path("profile/", ProfileList.as_view(), name="profile_list"),
    path("profile/<int:pk>/", ProfileDetail.as_view(), name="profile_detail")
]
