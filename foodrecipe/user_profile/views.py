from django.shortcuts import render

from .models import Profile
from main.models import User

# Create your views here.


def UserProfile(request):
    a={}
    userprofile=Profile.objects.all()
    # for i in userprofile:
    #    for j in i:
    #        print(j)
    print(userprofile)
    print(request.user)
    return render(request,'profile.html',{'userprofile': userprofile})
