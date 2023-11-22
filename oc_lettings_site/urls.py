from django.contrib import admin
from django.urls import path, include

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]

""" 
urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
"""
