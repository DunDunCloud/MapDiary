from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Place
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode
from .forms import PlaceForm

# Create your views here.
@login_required
def index(request):
    user = request.user

    # place = get_object_or_404(Place, name='place')
    # if user.is_authenticated:
    #     return redirect(index)
    # else:
    return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s'%(settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

@login_required
def new_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            form.save()
        return HttpResponseRedirect('index.html')
    
    else:
        form = PlaceForm()
    
    return render(request, 'index.html', {'form': form})


    return render(request, "index.html", {"form": form})
    # if request.method == 'POST':
    #     new_diary = Place.objects.create(
    #         title = request.POST['title'],
    #         description = request.POST['description'],
    #         writer = request.user.social_auth.get(provider='auth0').uid,
    #         lat = request.POST['lat'],
    #         lng = request.POST['lng']
    #     )
    # return render(request, 'index.html')
