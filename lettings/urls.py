from django.urls import path
from lettings.views import index, letting


urlpatterns = [
    path('', index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]