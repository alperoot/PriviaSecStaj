from django.urls import path

from .views import SignUpView
from Posts import views


urlpatterns = [
    path('kayit/', SignUpView.as_view(), name='kayit'),
]