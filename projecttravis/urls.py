from django.contrib import admin
from django.urls import path
from projecttravis.views import RequestStandings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RequestStandings.as_view()),
    path('iccstats', RequestStandings.as_view())
]
