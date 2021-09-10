from django.urls import path

from .views import AeroplaneApiView

urlpatterns = [
    path('aeroplane', AeroplaneApiView.as_view(), name='aeroplane'),
]
