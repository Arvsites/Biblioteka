from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = ''),
    path('about', views.about, name = 'about'),
    path('readers', views.readers, name = 'readers'),
    path('search', views.search, name = 'search'),
    path('events', views.events, name = 'events'),

]
