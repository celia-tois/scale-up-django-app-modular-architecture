from django.contrib import admin
from django.urls import path
from lettings.views import lettings_index, letting

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
