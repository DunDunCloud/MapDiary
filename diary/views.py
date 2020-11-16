from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Place
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode

# Create your views here.
@login_required
def index(request):
    user = request.user
    # place = get_object_or_404(Place, name='place')
    # if user.is_authenticated:
    #     return redirect(index)
    # else:
    return render(request, 'index.html', {'user': user, 'user_status': True})


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
def add_place(request):
    if request.method == 'POST':
        new_diary = Place.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            writer = request.user.social_auth.get(provider='auth0').uid,
            place_name = request.POST['place_name'],
            place_addr = request.POST['place_addr'],
            lat = request.POST['lat'],
            lng = request.POST['lng']
        )
        new_diary.save()
        print(new_diary)
    return render(request, 'index.html')


def add_good_place(request):
    context = {'status': 0,
               'message': 0,
               }
    return HttpResponse(json.dumps(context), content_type="application/json")

def show_place(request):
    uid = request.user.social_auth.get(provider='auth0').uid
    places = Place.objects.filter(writer=uid)

    return render(request, 'index.html', {'places':places})
