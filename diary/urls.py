from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPlace', views.add_place, name='add_place'),
    path('addplace', views.add_good_place, name='add_good_place'),
    path('showPlace', views.show_place, name='show_place'),
    path('delPost', views.delete_post, name='delete_post'),

    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]